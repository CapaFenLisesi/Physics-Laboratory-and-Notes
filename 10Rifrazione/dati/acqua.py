# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:45:18 2016

@author: zerch
"""


p= [48.5,43.5,41.5,38.5,34.5,33.5]
q= [43.5,45.5,56.5,63.5,82.5,86.5]

t=len(p)
a=[]
for i in range(0,t):
    a[i]=1./p[i]
    
print (a)