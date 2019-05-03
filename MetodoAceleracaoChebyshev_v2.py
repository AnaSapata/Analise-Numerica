'''
File: MetodoAceleracaoChebyshev_v2.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 05|Nov|2015
Version: 2.0
'''

import numpy as np
from numpy import linalg as la
import sympy as sy
from sympy import *

def polche(v,g):
    x=symbols('x')
    pol=[1,x]
    for i in range(2,g+1):
        n=len(pol)
        Tk=simplify(2*x*pol[n-1]-pol[n-2])
        pol.append(Tk)
    return pol[g].subs(x,v)

def cheb(A,b,x0,y0,it):
    yk0=y0
    yk1=0
    n=A.shape[0]
    P=np.zeros((n,n),dtype=float)
    for k in range(n):
        P[k,k]=np.diag(A)[k]
    N=P-A
    G=np.dot(la.inv(P),N)
    lambda_min=min(la.eigvals(G))
    lambda_max=max(la.eigvals(G))
    u=(2-lambda_max-lambda_min)/(lambda_max-lambda_min)
    i=2/(2-lambda_max-lambda_min)
    for j in range(it):
        if j==0:
            x1=np.array([[(G+la.inv(P)*b)[0,0]],[(G+la.inv(P)*b)[1,1]]])
            yk1=x1
            zk=np.matrix([[(la.inv(P)*b-np.dot(np.dot(la.inv(P),A),yk1))[0,0]],[(la.inv(P)*b-np.dot(np.dot(la.inv(P),A),yk1))[1,1]]])
        else:
            wk=(2*u*polche(u,j))/(polche(u,j+1))
            yk=yk0+np.dot(wk,(yk1-yk0+i*zk))
            yk0=yk1
            yk1=yk
            zk=np.matrix([[(la.inv(P)*b-np.dot(np.dot(la.inv(P),A),yk))[0,0]],[(la.inv(P)*b-np.dot(np.dot(la.inv(P),A),yk))[1,1]]])
    return yk

A=np.matrix([[2.,1.],[1.,2.]])
b=np.array([[3.],[3.]])
x0=np.matrix([[0.],[0.]])
y0=np.matrix([[0.],[0.]])
print "y3:\n"+str(cheb(A,b,x0,y0,3))
print "y9:\n"+str(cheb(A,b,x0,y0,9))
