# -*- coding: utf-8 -*-
''''
File: MetodoPotenciasInversas_v3(1)qq.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:19|Nov|2015
Version:3.1
'''

import numpy as np
from numpy import linalg as la

def matrizes():
    l=input("Numero de linhas:")
    c=input("Numero de colunas:")
    A=np.zeros((l,c),dtype=float)
    s=input("Simetrica? (S/N) ")
    if s=='S' or s=='s':
        for i in range (l):
            for j in range(i,c):
                A[i,j]=A[j,i]=round(np.random.uniform(-10,10),2)
    else:
        for i in range (l):
            for j in range (c):
                A[i,j]=round(np.random.uniform(-10,10),2)
    x0=np.zeros((l,1),dtype=float)
    x0[0,0]=1
    #for k in range(l):
        #x0[k,0]=round(np.random.uniform(-10,10),2)
    return A,x0

def potinv(A,sigma,x0,tol):
    n=A.shape[0]
    I=np.identity(n)
    A=np.squeeze(np.asarray(A))
    e=np.squeeze(np.asarray(la.eigvals(A)))
    v1=max(abs(e))
    n=e.shape[0]
    for i in range (n):
        if e[i]==v1 or e[i]==-v1:
            e[i]=0
    v2=max(abs(e))
    if abs(v2/v1)>0.70 and abs(v2/v1)<1:
        print "Converge rapidamente"
    elif abs(v1)==abs(v2):
        print "Não converge"
    elif abs(v2/v1)>=0 and abs(v2/v1)<=0.70:
        print "Converge lentamente"
    xk=np.squeeze(np.asarray(x0))
    vk=1
    vkk=2
    while abs(vkk-vk)/abs(vk)>tol or abs(vk-vkk)/abs(vkk)==tol:
        yk=la.solve((A-sigma*I),xk)
        vkk=vk
        vk=la.norm(yk,2)/la.norm(xk,2)
        xk=yk/la.norm(yk,2)
    return (1/vk)+sigma

A,x0=matrizes()
vk=potinv(A,0.5,x0,1.e-6)
print vk
print la.eigvals(A)
