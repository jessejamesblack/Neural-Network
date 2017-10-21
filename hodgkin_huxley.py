import scipy as sp
import pylab as pylab
from scipy import *
from pylab import *
from scipy.integrate import odeint

Cm = 1.0
gNa = 120.0
gk = 36.0
gL = 0.3
ENa = 50.0
EK = -77.0
EL = -54.387


def alpham(V): 
	return 0.1*(V+40.0)/(1.0 - sp.exp(-(V+40.0)/ 10.0))
def betam(V): 
	return 4.0*sp.exp(-(V+65.0)/18.0)
def alphah(V): 
	return 0.07*sp.exp(-(V+65.0) / 20.0)
def betah(V): 
	return 1.0/(1.0 + sp.exp(-(V+35.0)/10.0))
def alphan(V): 
	return 0.01*(V+55.0)/(1.0 - sp.exp(-(V+55.0)/10.0))
def betan(V): 
	return 0.125*sp.exp(-(V+65)/ 80.0)

def INa(V,m,h): return gNa * m**3 * h * (V-ENa)
def IK(V, n): return gk * n**4 *(V- EK)
def IL(V): return gL * (V - EL)
def Iinj(t): return 10*(t>100)-10*(t>200) + 35*(t>300)

t = sp.arange(0.0, 400.0, 0.1)

def integrate(X, t):
	V, m, h, n = X

	dVdt = (Iinj(t) - INa(V, m, h) - IK(V, n) - IL(V)) / Cm
	dmdt = alpham(V)*(1.0-m) - betam(V)*m
	dhdt = alphah(V)*(1.0-h) - betah(V)*h
	dndt = alphan(V)*(1.0-n) - betan(V)*n
	return dVdt, dmdt, dhdt, dndt

X = odeint(integrate, [-65, 0.05, 0.6, 0.32], t)
V = X[:, 0]
m = X[:, 1]
h = X[:, 2]
n = X[:, 3]
ina = INa(V,m,h)
ik = IK(V, n)
il = IL(V)

pylab.figure()
pylab.title('HH')
pylab.plot(t,V,'k', color = "blue")
pylab.ylabel('Voltage')
pylab.show()