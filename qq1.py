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

def RK21(y,t,h):
    yk=y+h*f(t+(h/2.),y+(h/2.)*f(t,y))
    return yk
#Experimentar em vez de RK21 o metodo Heun
def AB2(t0,T,h,u0):
    y=[u0]
    y.append(RK21(u0,t0,h))
    t=t0+h
    n=(T-t0)/h
    for i in range(1,int(n)):
        yk=y[i]+h*((3/2.)*f(t,y[i])-(1/2.)*f(t-h,y[i-1]))
        y.append(yk)
        t+=h
    return y

def AM2(t0,T,h,u0):
    y1=AB2(t0,T,h,u0)
    y2=[u0]
    y2.append(RK21(u0,t0,h))
    t=t0+h
    n=(T-t0)/h
    for i in range(1,int(n)):
        yk=y2[i]+(h/2.)*(f(t+h,y1[i+1])+f(t,y2[i]))
        y2.append(yk)
        t+=h
    return y2

t0=0
T=6
u0=2
h=0.25/16
sol1=AB2(t0,T,h,u0)
sol2=AM2(t0,T,h,u0)
print sol1
print sol2

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
plt.plot(r,sol1,'go',label='AB2')
plt.plot(r,sol2,'ro',label='AM2')

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
