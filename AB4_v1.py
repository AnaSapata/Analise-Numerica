''''
File: AB4_v1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:26|Nov|2015
Version:1.0
'''

import numpy as np
from numpy import linalg as la

def f(t,u):
    return (t-3.2)*u+8.*t*np.exp(0.5*((t-3.2)**2))*np.cos(4*t**2)

def exata(t):
    return np.exp(0.5*(t-3.2)**2)*np.sin(4.*t**2)

def RK41(t,y,h):
    F1=f(t,y)
    F2=f(t+0.5*h,y+0.5*h*F1)
    F3=f(t+0.5*h,y+0.5*h*F2)
    F4=f(t+h,y+h*F3)
    yk=y+(h/6)*(F1+2*F2+2*F3+F4)
    return yk

def AB4(t0,T,h,u0):
    t=t0
    n=(T-t0)/h
    y=[u0]
    for i in range(3):
        y.append(RK41(t,y[i],h))
        t+=h
    for k in range(3,int(n)+1):
        yk=y[k]+(h/24.)*(55*y[k]-59*y[k-1]+37*y[k-2]-9*y[k-3])
        y.append(yk)
    return y

t0=0
T=6
u0=2
h=0.25
print AB4(t0,T,h,u0)
n=(T-t0)/h
exac=[]
t=t0
for i in range(int(n)+2):
    exac.append(exata(t))
    t+=h
print exac
