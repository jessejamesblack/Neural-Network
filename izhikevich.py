from pylab import *

time = 500
dtdy = 1

a = 0.02
b = 0.2
c = -65
d = 8

l = 10
tr = array([200, 500]) / dtdy
tvec = arange(0, time, dtdy)

T = ceil(time / dtdy)
v = zeros(T)
u = zeros(T)
v[0] = -75
u[0] = -15

for t in arange(T - 1):
    if t > tr[0] and t < tr[1]:
        lh = l
    else:
        lh = 0
    if v[t] < 20:
        dvdt = (0.04 * v[t] + 5) * v[t] + 140 - u[t]
        v[t + 1] = v[t] + (dvdt + lh) * dtdy
        du = a * (b * v[t] - u[t])
        u[t + 1] = u[t] + dtdy * du
    else:
        v[t] = 35
        v[t + 1] = c
        u[t + 1] = u[t] + d

figure()
plot(tvec, v, 'b', label='Voltage', color = "blue")
xlabel('Time')
ylabel('V')
show()
