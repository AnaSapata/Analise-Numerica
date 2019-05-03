'''
Title: jacobi_v1.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 29|Out|2015
Version: 1.0
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
print Ad

Alu=A-Ad
print Alu

#k=0
x1=-(np.dot(np.dot(la.inv(Ad),Alu),x0))+la.inv(Ad)*b
print x1

#k=1
x2=-(np.dot(np.dot(la.inv(Ad),Alu),x1))+la.inv(Ad)*b
print x2

#k=2
x3=-(np.dot(np.dot(la.inv(Ad),Alu),x2))+la.inv(Ad)*b
print x3

#k=3
x4=-(np.dot(np.dot(la.inv(Ad),Alu),x3))+la.inv(Ad)*b
print x4

#k=4
x5=-(np.dot(np.dot(la.inv(Ad),Alu),x4))+la.inv(Ad)*b
print x5

print la.norm(-(np.dot(np.dot(la.inv(Ad),Alu),x1)),2)
