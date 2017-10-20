# topics
CS 443 / 525 Homework 1
1 Introduction
Neural models are a way to compute and capture certain properties of interest when simulating neural
networks. As we've seen, models vary in their complexity and realism, from modeling ion concentrations
explicitly, like Hodgkin-Huxley, to a simpler model we'll see below that only tracks membrane potential.
We can dene the change in membrane potential using a simple dierential equation like the following:
Cm
dV
dt
= I(t):
This is the integrate-and-re model (IF). Given a constant capitance Cm, it \integrates" time-dependent
inputs I(t) into the neuron's membrane potential V . Once the voltage exceeds a threshold voltage Vt, the
neuron \res" and the voltage is reset to the reset voltage Vr.
One problem with this model is that it continually integrates inputs until it reaches the threshold,
regardless of how long ago those inputs occurred. We can make this more realistic by introducing a current
\leak":
Cm
dV
dt
= I(t) 􀀀
Vm(t)
Rm
:
This is known as the leaky integrate-and-re model (LIF). Now we have a resistance parameter Rm as
well. This is sometimes written in the following form, where m = RmCm:
m
dV
dt
= 􀀀Vm(t) + RmI(t):
A slightly more realistic, but more complex, model is the Izhikevich model. It uses two variables { v to
track the cell voltage, and u, which can be thought of as a membrane recovery variable. It also has four
parameters, a; b; c, and d, which can be used to alter the cell's behavior to match various observed types of
biological neurons.
dv
dt
= 0:04v2 + 5v + 140 􀀀 u + I
du
dt
= a(bv 􀀀 u)
Then when v reaches 30 mV, the cell res, and then v is reset to c, and u increases by d.
Finally, one of the most detailed and realistic models is the Hodgkin-Huxley model, which models ion
concentrations directly, and for which voltage is modeled using the following equation:
C
dv
dt
= I 􀀀 gNam3h(V 􀀀 VNa) 􀀀 gKn4(V 􀀀 VK) 􀀀 gL(V 􀀀 VL)
For the full details of these models, please see the papers referenced below.
2 Questions
1. What do you expect to happen if an IF neuron is constantly fed a very low input current? An
LIF neuron?
2. What do you expect to happen if an IF neuron is constantly fed a larger input current? An LIF
neuron?
3. What are the limitations of an LIF neuron?
3 Programming
1. Simulate an LIF neuron with dierent input currents and plot the membrane potential, showing (a)
potential decay over time and (b) spiking behavior.
2. Plot the ring rate as a function of the input current.
3. What happens to the ring rate as you continue to increase the input current? Why?
4. Simulate a neuron using the Izhikevich model.
5. Simulate a neuron using the Hodgkin-Huxley model.
6. [BONUS - 10%] Assume that you administer a drug named TTX, which inhibits the sodium current. Simulate
the effect that TTX would have on the neural firing. Do the same for another drug, pronase, which eliminated
sodium inactivation.
Please return your answers in a concise report (5 p. max, including figures and code - the code should be selfexplanatory
and, if we have to, we should be able to run it as a script)
GOOD LUCK!
References
[1] Wulfram Gerstner. Time structure of the activity in neural network models. Physical review E, 51(1):738,
1995.
[2] Alan L Hodgkin and Andrew F Huxley. A quantitative description of membrane current and its appli-
cation to conduction and excitation in nerve. The Journal of physiology, 117(4):500{544, 1952.
[3] Eugene M Izhikevich. Simple model of spiking neurons. IEEE Transactions on neural networks,
14(6):1569{1572, 2003.
2
