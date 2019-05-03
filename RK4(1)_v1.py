''''
File: RK4(1)_v1.py
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

def RK41(t0,T,h,u0):
    y=[u0]
    n=(T-t0)/h
    t=t0
    for i in range(int(n)+1):
        F1=f(t,y[i])
        F2=f(t+0.5*h,y[i]+0.5*h*F1)
        F3=f(t+0.5*h,y[i]+0.5*h*F2)
        F4=f(t+h,y[i]+h*F3)
        yk=y[i]+(h/6)*(F1+2*F2+2*F3+F4)
        y.append(yk)
        t+=h
    return y

print RK41(0.,1.,0.25/18,2)
'''
t0=0
T=1
h=0.25/18
n=(T-t0)/h
exac=[]
t=t0
for i in range(int(n)+2):
    exac.append(exata(t))
    t+=h
print exac
'''
