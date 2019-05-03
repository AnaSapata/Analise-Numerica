'''
File: EulerProgressivo_v2(2).py
    -
Author: AnaSapata,ana_sapata@sapo.pt
Date: 13|Nov|2015
Version:2.2
'''

import numpy as np
import matplotlib.pyplot as plt

def f(t,u):
    return t*u

def exata(t):
    return np.exp(0.5*t**2+1)

def EulerProg(u0,h,t0,T,f):
    n=int((T-t0)/h)
    y=np.zeros(n)
    y=[u0]
    for i in range(n):
        tk=t0+(i-1)*h
        y[i]=y[i-1]+h*f(tk,y[i-1])
    return y


u0=2
h=0.25
t0=0
T=1

sol=EulerProg(u0,h,t0,T,f)
print sol
