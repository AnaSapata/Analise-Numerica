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
    return np.exp(0.5*t**2)+1

def EulerProg(u0,h,iin,ifi,f):
    yk=[u0]
    n=int((ifi-iin)/h)
    t=[iin]
    print"y0="+str(u0)
    for i in range(n):
        t.append(t[i]+h)
        yk.append(yk[i]+h*f(t[i],yk[i]))
        #print "y"+str(i+1)+"="+str(yk)
    return yk

u0=2
h=0.25
t0=0.
T=1.

sol=EulerProg(u0,h,t0,T,f)
print sol

N=int((T-t0)/h)+1

r=np.linspace(0.,1.,num=N)
print r

#To insert grid
#fig,ax=plt.subplots()
ax=plt.axes() #simpler...
ax.grid(True)

#All text and numbers in LaTeX...
plt.rc('text',usetex=False)
plt.rc('font',family='serif')

plt.plot(r,sol,'go',label='Approximated solution')
s=exata(r)
plt.plot(r,s,label='Exatc solution')

plt.axis([-0.2,1.2,1.5,3.5])
#plt.xlabel(r'\textbf{time}(s)',fontsize=16)
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"Euler's method", fontsize=20,color='blue',y=1.08)
#Adjust space for title
plt.subplots_adjust(top=0.8)

legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
#Put a nicer background color on the legend
legend.get_frame().set_facecolor('#00FFCC')

plt.show()
