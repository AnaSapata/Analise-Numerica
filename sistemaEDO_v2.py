# -*- coding: utf-8 -*-
''''
File: sistemaEDO_v2.py
    - RResolução de sistema de EDO's com o Euler Progressivo
Author: AnaSapata, ana_sapata@sapo.pt
Date:10|Dez|2015
Version:2.0
'''

import numpy as np
import matplotlib.pyplot as plt

def fx(tk,xk,yk):
    return -np.pi*yk

def fy(tk,xk,yk):
    return np.pi*xk

def exatax(t):
    return np.cos(np.pi*t)

def exatay(t):
    return np.sin(np.pi*t)

def EulerProg(x0,y0,h,t0,T):
    y=[y0]
    x=[x0]
    n=int((T-t0)/h)
    for i in range(n):
        tk=t0+i*h
        yk=y[i]+h*fy(tk,x[i],y[i])
        y.append(yk)
        xk=x[i]+h*fx(tk,x[i],y[i])
        x.append(xk)
    return y,x

x0=1
y0=0
h=0.1/10
t0=0
T=0.5

n=int((T-t0)/h)

soly,solx=EulerProg(x0,y0,h,t0,T)
print soly
print solx
N=int((T-t0)/h)+1

r=np.linspace(t0,T,num=N)

sx=exatax(r)
sy=exatay(r)

errox=sx-solx
erroy=sy-soly

ax=plt.axes()
ax.grid(True)

plt.rc('text',usetex=False)
plt.rc('font',family='serif')

plt.plot(r,soly,'r.',label='Approximated solution(y)')
plt.plot(r,sy,'r', label='Exact solution(y)')
plt.plot(r,solx,'b.',label='Approximated solution(x)')
plt.plot(r,sx,'b', label='Exact solution(x)')

plt.plot(r,errox,'g', label='Error(x)')
plt.plot(r,erroy,'m', label='Error(y)')

plt.axis([0.,0.5,-0.5,1.5])

plt.xlabel(r'time(s)',fontsize=16)

plt.title(r"Euler's method", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)

legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.show()
