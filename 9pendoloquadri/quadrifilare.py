# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:09:14 2016

@author: zerch
"""

import pylab
from scipy.optimize import curve_fit

# Lettura del file di dati in ingresso (da modificare con il percorso al
# vostro file in ingresso).
t, T, Tr = pylab.loadtxt('dati/pendoloquadrifilare0mod.txt', unpack = True)

# Definizione della geometria del pendolo [cm]
w = 1.91
l = 112.4
d = 114.7

# Calcolo di velocita' e angolo
v = (w/Tr)*(l/d)
Theta = pylab.arccos(1. - (v**2)/(2*980.*l))

# Funzioni di fit per velocita' e angolo
def f_v(x, v0, tau):
    return v0*pylab.exp(-x/tau)

def f_Theta(x, p1, p2):
    return 2*pylab.pi*pylab.sqrt(l/980.)*(1+ p1*(x**2) + p2*(x**4))

# Fit di V vs t
popt_v, pcov_v = curve_fit(f_v, t, v, pylab.array([500., 100.]))
v0_fit,   tau_fit = popt_v
dv0_fit, dtau_fit = pylab.sqrt(pcov_v.diagonal())
print('v0  = %f +- %f cm/s' % (v0_fit,  dv0_fit))
print('tau = %f +- %f s' % (tau_fit, dtau_fit))

# Plot di V vs t
pylab.figure(1)
pylab.xlabel('Tempo [s]') 
pylab.ylabel('v [cm/s]')
pylab.grid(color = 'gray')
pylab.plot(t, v, '+', label='data') 
pylab.plot(t, f_v(t, v0_fit, tau_fit), label='fit')
pylab.legend()
pylab.savefig('pendolo_VvsT.png')

# Plot di T vs Theta e dei residui rispetto alla funzione attesa
pylab.figure(2)
pylab.subplot(211)
pylab.ylabel('Periodo [s]') 
pylab.grid(color = 'gray')
pylab.plot(Theta, T, 'o', label='data') 
pylab.plot(Theta, f_Theta(Theta, 1./16, 11./3072), 'r', label='modello atteso')
pylab.legend(loc=2)
pylab.subplot(212)
pylab.xlabel('Angolo [rad]')
pylab.ylabel('Periodo data - modello [ms]') 
pylab.plot(Theta, 1000*(T-f_Theta(Theta, 1./16, 11./3072)))
pylab.grid(color = 'gray')

pylab.savefig('pendolo_TvsTheta.png')

pylab.show()