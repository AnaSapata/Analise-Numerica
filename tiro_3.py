# -*- coding: utf-8 -*-
''''
File: tiro_3.py
    - Resolução de EDO's de segunda ordem pelo metodo do tiro
Author: AnaSapata, ana_sapata@sapo.pt
Date:16|Dez|2015
Version:3.0
'''

import numpy as np
import matplotlib.pyplot as plt

def fy(tk,yk,wk):
    return wk

def fw(tk,yk,wk,b):
    if b==1:
        return (-2./tk)*wk+(2/(tk**2))*yk+np.sin(np.log(tk))/(tk**2)
    else:
        return (-2./tk)*wk+(2/(tk**2))*yk

def exata(t0,T,h):
    n=int((T-t0)/h)+1
    y=np.zeros(n)
    for i in range(n):
        t=t0+i*h
        c2=1./70.*(8-12*np.sin(np.log(2))-4*np.cos(np.log(2)))
        c1=11./10.-c2
        yk=c1*t+c2/(t**2)-3./10.*np.sin(np.log(t))-1./10.*np.cos(np.log(t))
        y[i]=yk
    return y

def RK42(y0,w0,h,t0,T,b):
    n=int((T-t0)/h)
    y=np.zeros(n+1)
    w=np.zeros(n+1)
    y[0]=y0
    w[0]=w0
    for i in range(n):
        t=t0+i*h
        F1y=fy(t,y[i],w[i])
        F1w=fw(t,y[i],w[i],b)
        F2y=fy(t+0.25*h,y[i]+0.25*h*F1y,w[i]+0.25*h*F1w)
        F2w=fw(t+0.25*h,y[i]+0.25*h*F1y,w[i]+0.25*h*F1w,b)
        F3y=fy(t+0.5*h,y[i]+0.5*h*F2y,w[i]+0.5*h*F2w)
        F3w=fw(t+0.5*h,y[i]+0.5*h*F2y,w[i]+0.5*h*F2w,b)
        F4y=fy(t+h,y[i]+h*F1y-2*h*F2y+2*h*F3y,w[i]+h*F1w-2*h*F2w+2*h*F3w)
        F4w=fw(t+h,y[i]+h*F1y-2*h*F2y+2*h*F3y,w[i]+h*F1w-2*h*F2w+2*h*F3w,b)
        y[i+1]=y[i]+(h/6)*(F1y+4*F3y+F4y)
        w[i+1]=w[i]+(h/6)*(F1w+4*F3w+F4w)
    return y,w

def final(y1,y2,t0,T,h,beta):
    n=int((T-t0)/h)
    y=np.zeros(n+1)
    c=(beta-y1[n])/y2[n]
    for i in range(n+1):
        y[i]=y1[i]+c*y2[i]
    return y

t0=1
T=2
h=0.25/16
y01=1
w01=0
y02=0
w02=1

y1,w1=RK42(y01,w01,h,t0,T,1)
y2,w2=RK42(y02,w02,h,t0,T,2)

#print "Solução do PVI1:\n Y1="+str(y1)+"\n W1="+str(w1)
#print "Solução do PVI2:\n Y2="+str(y2)+"\n W2="+str(w2)

yt=final(y1,y2,t0,T,h,2)
print "Solução pelo metodo do tiro:\n"+str(yt)
ye=exata(t0,T,h)
print "solução exata:\n"+str(ye)

n=int((T-t0)/h)

sol=yt
s=ye

N=int((T-t0)/h)+1

r=np.linspace(t0,T,num=N)

ax=plt.axes()
ax.grid(True)
plt.rc('text',usetex=False)
plt.rc('font',family='serif')
plt.plot(r,sol,'r.',label='Approximated solution(y)')
plt.plot(r,s,'r', label='Exact solution(y)')
plt.axis([0.95,2.05,0.95,2.05])
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"Metodo do tiro", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.show()
