from numpy import *
from pylab import *

T = 50
dt = 0.125
time = arange(0, T+dt, dt)
t_rest = 0

Vm = zeros(len(time))
Rm = 1
Cm = 10
tau_m = Rm*Cm
tau_ref = 4
Vth = 1
V_spike = 0.5

I = 1.5

for i, t in enumerate(time):
	if t > t_rest:
		Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
		if t >= Vth:
			Vm[i] += V_spike
			t_rest = t + tau_ref
plot(time, Vm)
ylabel('Voltage')
xlabel('Time')
ylim([0,2])
show()