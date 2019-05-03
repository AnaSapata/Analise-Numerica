# -*- coding: utf-8 -*-
''''
File: MetodoPotenciasDiretas_v3_1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:06|Nov|2015
Version:3.1
'''

import numpy as np
from numpy import linalg as la

def matrizes():
    l=input("Numero de linhas/colunas:")
    #c=input("Numero de colunas:")
    A=np.zeros((l,l),dtype=float)
    s=input("Simetrica? (S/N) ")
    if s=='S' or s=='s':
        for i in range (l):
            for j in range(i,l):
                A[i,j]=A[j,i]=round(np.random.uniform(-10,10),2)
    else:
        for i in range (l):
            for j in range (l):
                A[i,j]=round(np.random.uniform(-10,10),2)
    x0=np.zeros((l,1),dtype=float)
    for k in range(l):
        x0[k,0]=round(np.random.uniform(-10,10),2)
    return A,x0

def potdir(A,x0,tol):
    A=np.squeeze(np.asarray(A))
    e=np.squeeze(np.asarray(la.eigvals(A)))
    v1=max(abs(e))
    n=e.shape[0]
    for i in range (n):
        if e[i]==v1:
            e[i]=0
    v2=max(abs(e))
    if abs(v2/v1)>0.70 and abs(v2/v1)<1:
        print "Converge rapidamente"
    elif abs(v1)==abs(v2):
        print "Não converge"
    else:
        print "Converge lentamente"
    xk=np.squeeze(np.asarray(x0))
    vk=1
    vkk=2
    i=0
    while abs(vkk-vk)/abs(vk)>tol or abs(vk-vkk)/abs(vkk)==tol:
        yk=np.dot(A,xk)
        vkk=vk
        vk=np.inner(xk,yk)
        xk=yk/la.norm(yk,2)
        i+=1
    return vk,i

A,x0=matrizes()
print A
print x0
vk,i=potdir(A,x0,1.e-6)
print "\n"+str(max(abs(la.eigvals(A))))
print "\n"+str(vk)
print "\nn.º de iterações:"+str(i)
