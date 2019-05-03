'''
File: sistemaEDO_v02.py
    -
Author: AnaSapata,ana_sapata@sapo.pt
Date: 10|Dez|2015
Version:0.2
'''

import numpy as np

t0=0
T=0.5
#definir h
x0=1
y0=0

def EulerProg(u0,h,t0,T,f):
    yk=[u0]
    n=int((T-t0)/h)
    for i in range(n):
        t=t0+i*h
        yk.append(yk[i]+h*f(t,yk[i]))
    return yk

def fx(t):
    return -np.pi*fy(t)

def fy(t):
    return np.pi*fx(t)

x0=1
y0=0

def exata(t):
    x=np.cos(np.pi*t)
    y=np.sin(np.pi*t)
    return x,y
