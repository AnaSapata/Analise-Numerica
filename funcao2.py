''''
File: funcao2.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:2|Dez|2015
Version:1.0
'''

import numpy as np
from numpy import lianlg as la

def f(i,h):
    ai=1
    bi=2/(i*h)
    ci=-2/((i*h)**2)
    di=np.sen(np.log(i*h))/((i*h)**2)
    return ai,bi,ci,di

alfa=1
beta=2
t0=1
T=2

def exata(x):
    c2=1./70.*(8-12*np.sen(np.log(2))-4*np.cos(np.log(2)))
    c1=11./10.-c2
    y=c1*x+c2/(x**2)-3./10.*np.sen(np.log(x))-1./10.*np.cos(np.log(x))
    return y
