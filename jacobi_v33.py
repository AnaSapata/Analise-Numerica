# -*- coding: utf-8 -*-
'''
Title: jacobi_v3.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 29|Out|2015
Version: 3.0
'''

import numpy as np
from numpy import linalg as la

def matrizes():
    l=input("Numero de linhas/colunas:")
    #c=input("Numero de colunas:")
    #print (l,c)
    A=np.zeros((l,l),dtype=float)
    b=np.zeros((l,1),dtype=float)
    s=0
    for i in range (l):
        for j in range (l):
            A[i,j]=round(np.random.uniform(-10,10),2)
            if j!=i:
                s=s+abs(A[i,j])
        while abs(A[i,i]<s):
            A[i,i]=round(np.random.uniform(-10,10),2)
        b[i,0]=round(np.random.uniform(-10,10),2)
    return A,b

def diagdominante(A):
    n=A.shape[0]
    s=0
    for i in range(n):
        for j in range(n):
            if j!=i:
                s=s+abs(A[i,j])
        if abs(A[i,i]>s):
            return True
        else:
            return False

def Jacobi(A,b,x,it):
    n=A.shape[0]
    xk=x
    Ad=np.zeros((n,n),dtype=float)
    for k in range(n):
        Ad[k,k]=np.diagonal(A)[k]
    Alu=A-Ad
    #if la.norm(-(np.dot(la.inv(Ad),Alu)),2)>1 or la.norm(-(np.dot(la.inv(Ad),Alu)),2)==1:
    if diagdominante(A)==False:
        return "Não converge"
    else:
        for i in range(it):
            xk=-(np.dot(np.dot(la.inv(Ad),Alu),xk))+la.inv(Ad)*b
        return xk



A,b=matrizes()
print "A:\n"+str(A)+"\n"
print "b:\n"+str(b)+"\n"

#print diagdominante(A)

print "Solução:\n"+str(la.solve(A,b))+"\n"

x0=([[1.],[1.],[1.]])
print "x0:\n"+str(x0)+"\n"
print "Jacobi:\n"+str(Jacobi(A,b,x0,15))+"\n"
'''
A=np.matrix([[25.,1.,-3.5],[0.,9.4,-3.4],[1.,-1.,7.3]])
b=np.matrix([[5.],[-3.],[0.]])

A=np.matrix([[1.,2.,3.],[2.,3.,4.],[3.,4.,5.]])
b=np.matrix([[1.],[1.],[1.]])

print la.solve(A,b)

x0=([[1.],[1.],[1.]])
'''
