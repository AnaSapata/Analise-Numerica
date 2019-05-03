''''
File: AM2_v1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:26|Nov|2015
Version:1.0
'''

import numpy as np
import matplotlib.pyplot as plt

def f(t,u):
    return (t-3.2)*u+8.*t*np.exp(0.5*((t-3.2)**2))*np.cos(4*t**2)

def exata(t):
    return np.exp(0.5*(t-3.2)**2)*np.sin(4.*t**2)

def PredCorr(t0,T,h,u0):
    n=int((T-t0)/h)+1
    y=np.zeros(n)
    t=np.zeros(n)

    #RK21
    y[0]=u0
    t[0]=t0
    y[1]=y[0]+h*f(t[0]+(h/2.),y[0]+(h/2.)*f(t[0],y[0]))
    t[1]=t[0]+h

    for i in range(2,n):
        t[i]=t[i-1]+h
        #AB2
        y[i]=y[i-1]+h*((3/2.)*f(t[i-1],y[i-1])-(1/2.)*f(t[i-2],y[i-2]))
        #AM2
        y[i]=y[i-1]+(h/2.)*(f(t[i],y[i])+f(t[i-1],y[i-1]))
    return y

t0=0
T=6
u0=2
h=0.25/16
sol=PredCorr(t0,T,h,u0)
print sol

N=int((T-t0)/h)+1

r=np.linspace(0.,6.,num=N)
print r

#To insert grid
#fig,ax=plt.subplots()
ax=plt.axes() #simpler...
ax.grid(True)

#All text and numbers in LaTeX...
plt.rc('text',usetex=False)
plt.rc('font',family='serif')

#plt.figure(1)
plt.plot(r,sol,'go',label='Preditor Corretor')

#plt.figure(2)
s=exata(r)
plt.plot(r,s,label='Exatc solution')

plt.axis([0.,6.,-50.,50])
#plt.xlabel(r'\textbf{time}(s)',fontsize=16)
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"Euler's method", fontsize=20,color='blue',y=1.08)
#Adjust space for title
plt.subplots_adjust(top=0.8)

legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
#Put a nicer background color on the legend
legend.get_frame().set_facecolor('#00FFCC')

plt.show()
