# -*- coding: utf-8 -*-
''''
File: GradientesConjugados_v3(1(1)).py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:06|Nov|2015
Version:3.1.1
'''

import numpy as np
from numpy import linalg as la

#A=np.matrix([[3.,-1.,0.],[-1.,2.,-1.],[0.,1.,1.]])
#b=np.array([1.,0.,1.])


def matrizes():
    l=input("Numero de linhas/colunas:")
    positiva=False
    x=np.array([[1.],[1.],[1.]])
    A=np.zeros((l,l),dtype=float)
    b=np.zeros((l,1),dtype=float)
    p=[]
    m=0
    while (positiva==False):
        for i in range (l):
            for j in range(i,l):
                if j==i:
                    A[i,j]=round(np.random.uniform(0,10),2)
                else:
                    A[i,j]=A[j,i]=round(np.random.uniform(-10,10),2)
            b[i,0]=round(np.random.uniform(-10,10),2)
        for k in range(len(la.eigvals(A))):
            if la.eigvals(A)[k]<0:
                p.append(False)
            else:
                p.append(True)
        if False in p:
            positiva=False
            m+=1
            print m
    return A,b

def grad_conj(A,b,tol):
    n=A.shape[0]
    xk=np.squeeze(np.asarray(np.zeros((1,n),dtype=float)))
    rk=np.squeeze(np.asarray(-b))
    betak=0
    pk=np.squeeze(np.asarray(b))
    b=np.squeeze(np.asarray(b))
    while la.norm(rk,2)>tol or la.norm(rk,2)==tol:
        Apk=np.dot(A,pk)
        tauk=-(np.inner(pk,rk)/(np.inner(pk,Apk)))
        xk=xk+tauk*pk
        rk=np.squeeze(np.asarray(np.dot(A,xk)))-b
        betak=np.inner(rk,Apk)/np.inner(pk,Apk)
        pk=-rk-betak*pk
    return xk

A,b=matrizes()
print A
print b
print grad_conj(A,b,1.e-5)
print "exata:"+str(la.solve(A,b))
