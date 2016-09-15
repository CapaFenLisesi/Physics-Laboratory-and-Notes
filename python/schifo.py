# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:37:56 2016

@author: zerch
"""

"""
    y.insert(line, scipy.mean(dati))    
    erry.insert(line, scipy.std(dati))
    print y
    print erry
    

for line in txt:"""
    
"""
mainlist = []
infile = open('listtxt.txt','r')
for line in infile:
    mainlist.append(line.strip().split(','))

infile.close()

print mainlist
"""
"""
with open('datiprova.txt','r') as f:
    for line in f:
        dati=[]
        dati=[line]
        print dati
        y.insert(line, scipy.mean(dati))
"""