# -*- coding: utf-8 -*-
'''
File: Jacobi_v1.py
- Implementação do metodo de Jacobi
Author: AnaSapata, ana_sapata@sapo.pt
Date: 28|Out|2105
Version: 1.0
'''
import numpy as np
from numpy import linalg as la

def Jacobi(A,d,x,it):
    n=A.shape[0]
    Ad=np.zeros((n,n),dtype=float)
    for i in range (n):
        Ad[i,i]=np.diag(A)[i]
    Alu=A-Ad
    if la.norm(-(np.dot(la.inv(Ad),Alu)),2)<1:
        for k in range(it):
            x=-(np.dot((np.dot(la.inv(Ad),Alu)),x))+np.dot(la.inv(Ad),d)
        return x
    else:
        return "Não converge"

'''
A=np.matrix([[2.7,5.1,3.3],[-3.3,-0.6,5.7],[-1.8,+2.5,4.6]])
d=np.matrix([[-1.7],[3.6],[2.2]])
#print A
#print d
x=np.matrix([[1.],[1.],[1.]])
print la.solve(A,d)
print Jacobi(A,d,x,7)

A=np.matrix([[2.,-1.,1.],[3.,5.,-0.15],[0.04,-0.08,4.]])
d=np.matrix([[-3.],[9.],[20.]])
#print A
#print d
x=np.matrix([[1.],[1.],[1.]])
print la.solve(A,d)
print Jacobi(A,d,x,20)

A=np.matrix([[3.,-1.,3],[-2.,3.,-4.],[1.,-1.,4.]])
d=np.matrix([[0.],[8.],[5.]])
#print A
#print d
x=np.matrix([[1.],[1.],[1.]])
print la.solve(A,d)
print Jacobi(A,d,x,7)
'''
