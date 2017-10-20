import scipy as sp
import pylab as pylab
from scipy import *
from pylab import *
from scipy.integrate import odeint

C_m = 1.0
g_Na = 120.0
g_k = 36.0
g_L = 0.3
E_Na = 50.0
E_K = -77.0
E_L = -54.387


def alpha_m(V): return 0.1*(V+40.0)/(1.0 - sp.exp(-(V+40.0)/ 10.0))
def beta_m(V): return 4.0*sp.exp(-(V+65.0)/18.0)
def alpha_h(V): return 0.07*sp.exp(-(V+65.0) / 20.0)
def beta_h(V): return 1.0/(1.0 + sp.exp(-(V+35.0)/10.0))
def alpha_n(V): return 0.01*(V+55.0)/(1.0 - sp.exp(-(V+55.0)/10.0))
def beta_n(V): return 0.125*sp.exp(-(V+65)/ 80.0)

def I_Na(V,m,h): return g_Na * m**3 * h * (V-E_Na)

def I_K(V, n): return g_k * n**4 *(V- E_K)

def I_L(V): return g_L * (V - E_L)

def I_inj(t): return 10*(t>100)-10*(t>200) + 35*(t>300)

t = sp.arange(0.0, 400.0, 0.1)

def dALLdt(X, t):
	V, m, h, n = X

	dVdt = (I_inj(t) - I_Na(V, m, h) - I_K(V, n) - I_L(V)) / C_m
	dmdt = alpha_m(V)*(1.0-m) - beta_m(V)*m
	dhdt = alpha_h(V)*(1.0-h) - beta_h(V)*h
	dndt = alpha_n(V)*(1.0-n) - beta_n(V)*n
	return dVdt, dmdt, dhdt, dndt

X = odeint(dALLdt, [-65, 0.05, 0.6, 0.32], t)
V = X[:, 0]
m = X[:, 1]
h = X[:, 2]
n = X[:, 3]
ina = I_Na(V,m,h)
ik = I_K(V, n)
il = I_L(V)

pylab.figure()
pylab.title('HH')
pylab.plot(t,V,'k')
pylab.ylabel('Voltage')

pylab.show()