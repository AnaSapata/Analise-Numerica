# -*- coding: utf-8 -*-
''''
File: sistemaEDO_v6.py
    - Resolução de sistema de EDO's pelos dois metodos com os dois graficos
Author: AnaSapata, ana_sapata@sapo.pt
Date:10|Dez|2015
Version:6.0
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as s
from scipy import stats

def fx(tk,xk,yk):
    return -np.pi*yk

def fy(tk,xk,yk):
    return np.pi*xk

def exatax(t):
    return np.cos(np.pi*t)

def exatay(t):
    return np.sin(np.pi*t)

def RK42(x0,y0,h,t0,T):
    n=int((T-t0)/h)
    y=np.zeros(n+1)
    x=np.zeros(n+1)
    y[0]=y0
    x[0]=x0
    for i in range(n):
        t=t0+i*h
        F1y=fy(t,x[i],y[i])
        F1x=fx(t,x[i],y[i])
        F2y=fy(t+0.25*h,x[i]+0.25*h*F1x,y[i]+0.25*h*F1y)
        F2x=fx(t+0.25*h,x[i]+0.25*h*F1x,y[i]+0.25*h*F1y)
        F3y=fy(t+0.5*h,x[i]+0.5*h*F2x,y[i]+0.5*h*F2y)
        F3x=fx(t+0.5*h,x[i]+0.5*h*F2x,y[i]+0.5*h*F2y)
        F4y=fy(t+h,x[i]+h*F1x-2*h*F2x+2*h*F3x,y[i]+h*F1y-2*h*F2y+2*h*F3y)
        F4x=fx(t+h,x[i]+h*F1x-2*h*F2x+2*h*F3x,y[i]+h*F1y-2*h*F2y+2*h*F3y)
        y[i+1]=y[i]+(h/6)*(F1y+4*F3y+F4y)
        x[i+1]=x[i]+(h/6)*(F1x+4*F3x+F4x)
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

m1x, b1x, r_value, p_value, std_err = stats.linregress(r,eerrox)
m1y, b1y, r_value, p_value, std_err = stats.linregress(r,eerroy)
m2x, b2x, r_value, p_value, std_err = stats.linregress(r,rerrox)
m2y, b2y, r_value, p_value, std_err = stats.linregress(r,rerroy)

def mmq(x, y):
    u"""
    x é uma matriz com as variáveis independentes
    y é um array com a variável dependente
    O retorno é um array contendo os valores dos beta's
    """
    x = np.insert(x, 0, 1, axis=1)
    x_t = np.transpose(x)
    xt_x = np.dot(x_t, x)
    inverse_xt_x = np.linalg.inv(xt_x)
    xt_y = np.dot(x_t, y)
    return np.dot(inverse_xt_x, xt_y)

#beta=mmq(r,eerrox)
#print beta
#print "compa beta/b:",beta[0]==b1x
#print "compa beta/m:",beta[1]==m1x
def regressao(m,x,b):
    return m*x+b

reg1x=regressao(m1x,r,b1x)
reg1y=regressao(m1y,r,b1y)
reg2x=regressao(m2x,r,b2x)
reg2y=regressao(m2y,r,b2y)

plt.figure(1)
ax=plt.axes()
ax.grid(True)
plt.rc('text',usetex=False)
plt.rc('font',family='serif')
plt.plot(r,esoly,'r.',label='Approximated solution(y)')
plt.plot(r,sy,'r', label='Exact solution(y)')
plt.plot(r,esolx,'b.',label='Approximated solution(x)')
plt.plot(r,sx,'b', label='Exact solution(x)')
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
plt.plot(r,eerrox,'r.', label='Error (x)')
plt.plot(r,eerroy,'b.', label='Error (y)')
plt.plot(r,reg1x,'r', label='Reta de regressao linear (x)')
plt.plot(r,reg1y,'b', label='Reta de regressao linear (y)')
plt.axis([0.,0.5,-1.e-1,1.e-1])
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"Erro pelo metodo Euler", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.figure(3)
ax=plt.axes()
ax.grid(True)
plt.rc('text',usetex=False)
plt.rc('font',family='serif')
plt.plot(r,rsoly,'r.',label='Approximated solution(y)')
plt.plot(r,sy,'r', label='Exact solution(y)')
plt.plot(r,rsolx,'b.',label='Approximated solution(x)')
plt.plot(r,sx,'b', label='Exact solution(x)')
plt.axis([0.,0.5,-0.5,1.5])
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"RK42", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.figure(4)
ax=plt.axes()
ax.grid(True)
plt.rc('text',usetex=False)
plt.rc('font',family='serif')
plt.plot(r,rerrox,'r.', label='Error (x)')
plt.plot(r,rerroy,'b.', label='Error (y)')
plt.plot(r,reg2x,'r', label='Reta de regressao linear (x)')
plt.plot(r,reg2y,'b', label='Reta de regressao linear (y)')
plt.axis([0.,0.5,-1.e-7,1.e-7])
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"Erro pelo RK4/2", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.show()
