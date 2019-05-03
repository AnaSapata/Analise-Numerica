# -*- coding: utf-8 -*-
''''
File: DiferençasFinitas_v3.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:16|Dez|2015
Version:3.0
'''

import numpy as np
import matplotlib.pyplot as plt

'''
def f(i,h):
    ai=(i*h)**2+1
    bi=(2*i*h)
    ci=np.sin(i*h)
    di=np.cos(i*h)
    return ai,bi,ci,di
'''
def f(t0,i,h):
    ai=1
    bi=2/(t0+i*h)
    ci=-2/((t0+i*h)**2)
    di=np.sin(np.log(t0+i*h))/((t0+i*h)**2)
    return ai,bi,ci,di

def diffin(t0,T,h,alfa,beta):
    n=int((T-t0)/h)
    #A=np.zeros((n,n),dtype=float)
    A=np.zeros((n-1,n-1),dtype=float)
    #b=np.zeros((n,1),dtype=float)
    b=np.zeros(n-1)
    for k in range(1,n):
        ai,bi,ci,di=f(t0,k,h)
        pi=-(ci*(h**2))+2*ai
        qi=-ai-0.5*bi*h
        ri=-ai+0.5*bi*h
        if k==1:
            A[k-1,k-1]=pi
            A[k-1,k]=qi
            b[k-1]=(-h**2)*(di+(ri/h**2)*alfa)
        elif k==(n-1):
            A[k-1,k-1]=pi
            A[k-1,k-2]=ri
            b[k-1]=(-h**2)*(di+(qi/h**2)*beta)
        else:
            A[k-1,k-2]=ri
            A[k-1,k-1]=pi
            A[k-1,k]=qi
            b[k-1]=-(h**2)*(di)
    return A,b

def alfa_beta(A,d):
    n=A.shape[0]
    alfa=np.zeros(n-1)
    beta=np.zeros(n)
    for k in range (n):
        if k==0:
            alfa[k]=-(A[k,k+1]/A[k,k])
            beta[k]=d[k]/A[k,k]
        elif k>0 and k<n-1:
            alfa[k]=-(A[k,k+1]/(A[k,k-1]*alfa[k-1]+A[k,k]))
            beta[k]=(d[k]-A[k,k-1]*beta[k-1])/(A[k,k-1]*alfa[k-1]+A[k,k])
        else:
            beta[k]=(d[k]-A[k,k-1]*beta[k-1])/(A[k,k-1]*alfa[k-1]+A[k,k])
    return alfa, beta

def sistema(A,d,alfa,beta):
    d1=np.squeeze(np.asarray(d))
    n=A.shape[0]
    x=np.zeros(n+2)
    alfa1,beta1=alfa_beta(A,d1)
    for k in range (n+2):
        if k==1:
            x[n-k+1]=beta1[n-k]
        elif k==0:
            x[n-k+1]=beta
        elif k==n+1:
            x[n-k+1]=alfa
        else:
            x[n-k+1]=alfa1[n-k]*x[n-k+2]+beta1[n-k]
    return np.squeeze(np.asarray(x))


'''
t0=0
T=1
h=0.10
alfa=0
beta=1
'''
def exata(t0,T,h):
    x=[]
    n=int((T-t0)/h)+1
    y=np.zeros(n)
    for i in range(n):
        x.append(t0+i*h)
    for k in range(n):
        c2=1./70.*(8-12*np.sin(np.log(2))-4*np.cos(np.log(2)))
        c1=11./10.-c2
        yk=c1*x[k]+c2/(x[k]**2)-3./10.*np.sin(np.log(x[k]))-1./10.*np.cos(np.log(x[k]))
        y[k]=yk
    return y

alfa=1
beta=2
h=0.25/8
t0=1
T=2

A,b=diffin(t0,T,h,alfa,beta)
#print A
#print b
print "Solução das matrizes pelo tridiagonal:\n"+str(sistema(A,b,alfa,beta))
#print "Solução da matriz:\n"+str(la.solve(A,b))
print "Solução exata:\n"+str(exata(t0,T,h))
erro=exata(t0,T,h)-sistema(A,b,alfa,beta)
#print "Erro:\n"+str(erro)



n=int((T-t0)/h)

sol=sistema(A,b,alfa,beta)
s=exata(t0,T,h)

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
plt.title(r"Diferencas Finitas", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.show()
