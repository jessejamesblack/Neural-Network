from numpy import *
from pylab import *

## setup parameters and state variables
T       = 10                  # total time to simulate (msec)
dt      = 0.1               # simulation time step (msec)
time    = arange(0, T+dt, dt) # time array
t_rest  = 0                   # initial refractory time

## LIF properties
Vm      = zeros(len(time))    # potential (V) trace over time
Rm      = 1                   # resistance (kOhm)
Cm      = 5                  # capacitance (uF)
tau_m   = Rm*Cm               # time constant (msec)
tau_ref = 2                   # refractory period (msec)
Vth     = 1                   # spike threshold (V)
V_spike = 1                # spike delta (V)

## Stimulus
I       = .5                 # input current (A)

## iterate over each time step
for i, t in enumerate(time):
	if t > t_rest:
  		Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
		if t >= Vth:
    			Vm[i] += V_spike
    			t_rest = t + tau_ref

## plot membrane potential trace
plot(time, Vm)
ylabel('MP')
xlabel('Time')
show()
