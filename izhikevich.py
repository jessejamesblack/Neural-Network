from pylab import *

tmax = 1000
dt = 1

a = 0.02
b = 0.2
c = -65
d = 8

lapp = 10
tr = array([200, 700])/dt 
 
T = ceil(tmax / dt)
v = zeros(T)
u = zeros(T)
v[0] = -70 
u[0] = -14 
 
for t in arange(T-1):
    if t > tr[0] and t < tr[1]:
        l = lapp
    else:
        l = 0
    if v[t] < 35:
        dv = (0.04*v[t]+5)*v[t]+140-u[t]
        v[t+1] = v[t]+(dv+l)*dt
        du = a*(b*v[t]-u[t])
        u[t+1] = u[t] + dt*du
    else:
        v[t] = 35
        v[t+1] = c
        u[t+1] = u[t] + d
        
figure()
tvec = arange(0, tmax, dt)
plot(tvec, v, 'b', label='Voltage')
xlabel('Time')
ylabel('mV')
show()
