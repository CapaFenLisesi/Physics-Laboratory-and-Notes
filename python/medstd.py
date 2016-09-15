# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:55:42 2016

@author: zerch
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.optimize
import scipy.stats
import os
import pylab
"""

dati=[16.04, 16.00 , 16.01 , 16.09 , 16.07 , 16.10 , 16.03 , 16.08 , 16.09 , 16.01]

mean=scipy.mean(dati)

std=np.std(dati,ddof=1)

sem=scipy.stats.sem(dati)

print (mean)
print (std)
print (sem)
"""

#Legge ogni riga come un array 
f=np.loadtxt('/home/zerch/Documents/UNIPI/LAB1/6Penfisico/grafici/periodi.txt')
print (f)

mean=scipy.mean(f,axis=1) #fa la media riga per riga di unna matrice

std=np.std(f,axis=1)

sem=scipy.stats.sem(f,axis=1)

print (mean)
print (std)
print (sem)


 