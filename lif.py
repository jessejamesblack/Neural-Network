from numpy import *
from pylab import *

TV = 50
dtdy = 0.125
time = linespace(0, TV+dtdy, dtdy, endpoint=True)
timeout = 0

V = zeros(len(time))
R = 1
C = 10
tau = R*C
taur = 4
Vth = 1
Vspike = 0.5

I = 1.5

for i in range(time(len(j):
	if TV > timeout:
		V[i] = V[i-1] + (-V[i-1] + I*R) / tau * dtdy
		if j >= Vth:
			V[i] += Vspike
			timeout = j + taur
plot(time, Vm)
ylabel('Voltage')
xlabel('Time')
ylim([0,2])
show()
