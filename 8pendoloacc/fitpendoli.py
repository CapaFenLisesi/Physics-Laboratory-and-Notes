# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:40:38 2016

@author: zerch
"""

import pylab
from scipy.optimize import curve_fit

# Lettura del file di dati in ingresso (da modificare con il percorso al
# vostro file in ingresso).
t, A, B = pylab.loadtxt('dati/battimenti.txt', unpack = True)

# Selezione dell'intervallo di tempo per il fit:
t_min = 100
t_max = 150

# Extrazione dei dati corrispondenti all'intervallo di tempo selezionato
t1 = t[t>t_min];  st = t1[t1<t_max];  
A1 = A[t>t_min];  sA = A1[t1<t_max]; 
B1 = B[t>t_min];  sB = B1[t1<t_max]; 

# Per prima cosa guardiamo i grafici dei due pendoli
pylab.figure(1)
pylab.subplot(211)
pylab.ylabel('Pendolo A [u.a.]')
pylab.grid(color = 'gray')
pylab.plot(t, A)
pylab.plot(st, sA, 'r') 
pylab.subplot(212)
pylab.xlabel('Tempo [s]') 
pylab.ylabel('Pendolo B [u.a.]')
pylab.grid(color = 'gray')
pylab.plot(t, B, 'g')
pylab.plot(st, sB, 'r') 
pylab.show()

# Funzione di fit: oscillatore armonico smorzato
def f(x, A, omega, tau, p, c):
    return A*pylab.exp(-x/tau)*pylab.cos(omega*x +p) + c

# Inizializzazione dei parametri per il pendolo A
# Attenzione: partire da un set di parametri appropriati e' fondamentale 
#             per la convergenza del fit
initParamsA = pylab.array([500., 4.4, 70., 0., 480.])

# Fit del pendolo A nell'intervallo selezionato
popt_A, pcov_A = curve_fit(f, st, sA, initParamsA)
A_fit,   omega_fit_A,  tau_fit_A,  p_fit_A,  c_fit_A = popt_A
dA_fit, domega_fit_A, dtau_fit_A, dp_fit_A, dc_fit_A = pylab.sqrt(pcov_A.diagonal())
print('Omega = %f +- %f rad/s' % (omega_fit_A, domega_fit_A))
print('Tau   = %f +- %f s'     % (tau_fit_A,   dtau_fit_A))

# il fit del pendolo B si esegue allo stesso modo....

# Realizzazione e salvataggio del grafico A
pylab.figure(2)
pylab.xlabel('Tempo [s]') 
pylab.ylabel('Pendolo A [u.a.]')
pylab.grid(color = 'gray')
pylab.plot(st, sA, '+', label='data') 
pylab.plot(st, f(st, A_fit,   omega_fit_A,  tau_fit_A,  p_fit_A,  c_fit_A), label='fit')
pylab.legend()
pylab.savefig('pendoloA_fit.png')
pylab.show()