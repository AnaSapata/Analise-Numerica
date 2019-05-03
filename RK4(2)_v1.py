''''
File: RK4(2)_v1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:2|Dez|2015
Version:1.0
'''
#Fazer o calculo do erro
import numpy as np
import matplotlib.pyplot as plt
import funcao1 as fc

def RK42(t0,T,h,u0):
    y=[u0]
    n=(T-t0)/h
    t=t0
    for i in range(int(n)):
        F1=fc.f(t,y[i])
        F2=fc.f(t+0.25*h,y[i]+0.25*h*F1)
        F3=fc.f(t+0.5*h,y[i]+0.5*h*F2)
        F4=fc.f(t+h,y[i]+h*F1-2*h*F2+2*h*F3)
        yk=y[i]+(h/6)*(F1+4*F3+F4)
        y.append(yk)
        t+=h
    return y

sol=RK42(fc.t0,fc.T,fc.h,fc.u0)
print sol

N=int((fc.T-fc.t0)/fc.h)+1

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
plt.plot(r,sol,'yo',label='Approximated solution')

#plt.figure(2)
s=fc.exata(r)
plt.plot(r,s,'r', label='Exatc solution')

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
