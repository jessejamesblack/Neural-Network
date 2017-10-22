from numpy import *
from pylab import *

#params and vars
TV = 10
dtdy = 0.1
time = arange(0, TV + dtdy, dtdy)
timeout = 0

#properties of the neuron
trace = zeros(len(time))
resistance = 1
capa = 5
timeConst = resistance * capa
refracPer = 2
threshold = 1
spikeDelta = .5

#input stimulus
stimulus = .5


for stimulus, timeStep in enumerate(time):
	if TV > timeout:
		trace[stimulus] = trace[stimulus - 1] + (-trace[stimulus - 1] + stimulus * resistance) / timeConst * dtdy
		if timeStep >= threshold:
         	   	trace[stimulus] += spikeDelta
    			timeout = timeStep + refracPer
plot(time, trace)
ylabel('MP')
xlabel('Time')
show()
