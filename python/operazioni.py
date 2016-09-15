# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:17:35 2016

@author: zerch
"""
import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.optimize
import scipy.stats
import os
import pylab

y=[]
dati = [] #inizializziamo il vettore dove mettiamo le misure
periodi=[1.631,1.563,1.558,1.678,2.268,3.805,1.851,1.595,1.567,1.605]
for i in range(0,10):
    misura = float(input("Immettere misura acquisita: "))
    dati.insert(i,misura)
    print (dati)
    y.insert(i, 2*(dati[i])*(periodi[i]))
print (y)