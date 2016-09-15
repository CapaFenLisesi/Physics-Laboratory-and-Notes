# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:08:11 2016

@author: zerch
"""
import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.optimize
import scipy.stats
import os
import pylab

y = []
erry=[]
data=[]



with open('datiprova.txt','r') as f