from numpy import *
from pylab import *

TV = 25
dtdy = 0.5
time = arange(0, TV+dtdy, dtdy)
timeout = 0

V = zeros(len(time))
R = 1
C = 5
tau = R*C
taur = 2
Vth = 1
Vspike = 1

I = 2


for i, t in enumerate(time):
	if TV > timeout:
		V[i] = V[i-1] + (-V[i-1] + I*R) / tau * dtdy
		if t >= Vth:
			V[i] += Vspike
	timeout = t + taur
plot(time, V)
ylabel('Voltage')
xlabel('Time')
ylim([0,50])
show()
