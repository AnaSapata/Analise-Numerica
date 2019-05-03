# -*- coding: utf-8 -*-
'''
Title: jacobi_v2.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 29|Out|2015
Version: 2.0
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[25.,1.,-3.5],[0.,9.4,-3.4],[1.,-1.,7.3]])
b=np.matrix([[5.],[-3.],[0.]])

print la.solve(A,b)

x0=([[1.],[1.],[1.]])

Ad=np.zeros((3,3),dtype=float)
Ad[0,0]=np.diagonal(A)[0]
Ad[1,1]=np.diagonal(A)[1]
Ad[2,2]=np.diagonal(A)[2]
#print Ad

Alu=A-Ad
#print Alu
def Jacobi(Ad,Alu,b,x,it):
    xk=x
    if la.norm(-(np.dot(la.inv(Ad),Alu)),2)>1 or la.norm(-(np.dot(la.inv(Ad),Alu)),2)==1:
        return "Não converge"
    else:
        for i in range(it):
            xk=-(np.dot(np.dot(la.inv(Ad),Alu),xk))+la.inv(Ad)*b
        return xk

print
print Jacobi(Ad,Alu,b,x0,5)
