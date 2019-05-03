# -*- coding: utf-8 -*-
'''
Title: Gauss_v1.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 29|Out|2015
Version: 1.0
'''

import numpy as np
from numpy import linalg as la


A=np.matrix([[25.,1.,-3.5],[0.,9.4,-3.4],[1.,-1.,7.3]])
b=np.matrix([[5.],[-3.],[0.]])
'''
A=np.matrix([[1.,2.,3.],[2.,3.,4.],[3.,4.,5.]])
b=np.matrix([[1.],[1.],[1.]])
'''
print la.solve(A,b)

x0=([[1.],[1.],[1.]])

def Jacobi(A,b,x,it):
    n=A.shape[0]
    xk=x
    Ad=np.zeros((n,n),dtype=float)
    for k in range(n):
        Ad[k,k]=np.diagonal(A)[k]
    Alu=A-Ad
    if la.norm(-(np.dot(la.inv(Ad),Alu)),2)>1 or la.norm(-(np.dot(la.inv(Ad),Alu)),2)==1:
        return "Não converge"
    else:
        for i in range(it):
            xk=-(np.dot(np.dot(la.inv(Ad),Alu),xk))+la.inv(Ad)*b
        return xk

print
print Jacobi(A,b,x0,15)
