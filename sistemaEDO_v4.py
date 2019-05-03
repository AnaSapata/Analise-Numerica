# -*- coding: utf-8 -*-
''''
File: sistemaEDO_v4.py
    - Resolução de sistema de EDO's pelos dois metodos com os dois graficos
Author: AnaSapata, ana_sapata@sapo.pt
Date:10|Dez|2015
Version:4.0
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

def RK42(x0,y0,h,t0,T):
    #y=[y0]
    #x=[x0]
    n=int((T-t0)/h)
    y=np.zeros(n+1)
    x=np.zeros(n+1)
    y[0]=y0
    x[0]=x0
    #t=t0
    for i in range(n):
        t=t0+i*h
        #para calcular o yk+1
        F1y=fy(t,x[i],y[i])
        F2y=fy(t+0.25*h,x[i]+0.25*h*F1y,y[i]+0.25*h*F1y)
        F3y=fy(t+0.5*h,x[i]+0.5*h*F2y,y[i]+0.5*h*F2y)
        F4y=fy(t+h,x[i]+h*F1y-2*h*F2y+2*h*F3y,y[i]+h*F1y-2*h*F2y+2*h*F3y)
        y[i+1]=y[i]+(h/6)*(F1y+4*F3y+F4y)
        #para calcular o xk+1
        F1x=fx(t,x[i],y[i])
        F2x=fx(t+0.25*h,x[i]+0.25*h*F1x,y[i]+0.25*h*F1x)
        F3x=fx(t+0.5*h,x[i]+0.5*h*F2x,y[i]+0.5*h*F2x)
        F4x=fx(t+h,x[i]+h*F1x-2*h*F2x+2*h*F3x,y[i]+h*F1x-2*h*F2x+2*h*F3x)
        x[i+1]=x[i]+(h/6)*(F1x+4*F3x+F4x)
        #x.append(xk)
        #t+=h
    return y,x

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

esoly,esolx=EulerProg(x0,y0,h,t0,T)
rsoly,rsolx=RK42(x0,y0,h,t0,T)

N=int((T-t0)/h)+1

r=np.linspace(t0,T,num=N)

sx=exatax(r)
sy=exatay(r)

eerrox=sx-esolx
eerroy=sy-esoly

rerrox=sx-rsolx
rerroy=sy-rsoly



plt.figure(1)
ax=plt.axes()
ax.grid(True)
plt.rc('text',usetex=False)
plt.rc('font',family='serif')
plt.plot(r,esoly,'r.',label='Approximated solution(y)')
plt.plot(r,sy,'r', label='Exact solution(y)')
plt.plot(r,esolx,'b.',label='Approximated solution(x)')
plt.plot(r,sx,'b', label='Exact solution(x)')
plt.plot(r,eerrox,'g', label='Error(x)')
plt.plot(r,eerroy,'m', label='Error(y)')
plt.axis([0.,0.5,-0.5,1.5])
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"Euler's method", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.figure(2)
ax=plt.axes()
ax.grid(True)
plt.rc('text',usetex=False)
plt.rc('font',family='serif')
plt.plot(r,rsoly,'r.',label='Approximated solution(y)')
plt.plot(r,sy,'r', label='Exact solution(y)')
plt.plot(r,rsolx,'b.',label='Approximated solution(x)')
plt.plot(r,sx,'b', label='Exact solution(x)')
plt.plot(r,rerrox,'g', label='Error(x)')
plt.plot(r,rerroy,'m', label='Error(y)')
plt.axis([0.,0.5,-0.5,1.5])
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"RK42", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.show()
