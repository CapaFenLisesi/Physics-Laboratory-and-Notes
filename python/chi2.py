# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:05:01 2016

@author: zerch
"""

import numpy 
import scipy 
import scipy.stats
import math

Chi2 = 1010
ndof = 9
p = (scipy.stats.chi2.cdf(Chi2,ndof))
 
print (p)