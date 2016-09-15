# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:46:09 2016

@author: zerch
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.optimize
import scipy.stats
import os
import pylab


#MEDIA DI TUTTE LE MISURE
y = []
erry=[]
numpunti=10

numdati= 3 #numero di misure fatte di un punto
for i in range(0,numpunti):
    dati = [] #inizializziamo il vettore dove mettiamo le misure
    for j in range(0,numdati):
        misura = float(input("Immettere misura acquisita: "))
        dati.insert(j,misura)
        print (dati)
    y.insert(i, scipy.mean(dati))    
    erry.insert(i, scipy.std(dati))
    print (y)
    print (erry)
    
#ABBIAMO CREATO IL VETTORE CON LE ORDINATE Y DEL NOSTRO GRAFICO

