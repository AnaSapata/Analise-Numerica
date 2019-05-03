'''
File: MetodoAceleracaoChebyshev_v1_1.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 05|Nov|2015
Version: 1.1
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[2.,1.],[1.,2.]])
print "A:\n"+str(A)

P=np.zeros((2,2),dtype=float)
P[0,0]=np.diag(A)[0]
P[1,1]=np.diag(A)[1]
print "P:\n"+str(P)

N=P-A
print "N:\n"+str(N)

G=np.dot(la.inv(P),N)
print "G:\n"+str(G)

print la.eigvals(G)
lambda_min=min(la.eigvals(G))
print lambda_min
lambda_max=max(la.eigvals(G))
print lambda_max

x0=np.array([[0.],[0.]])
y0=np.array([[0.],[0.]])
print "x0:\n"+str(x0)
print "y0:\n"+str(y0)

u=(2-lambda_max-lambda_min)/(lambda_max-lambda_min)
print "u:\n"+str(u)

i=2/(2-lambda_max-lambda_min)
print "i:\n"+str(i)

T0u=1
T1u=np.polynomial.chebyshev.chebvander(u,1)[0,1]
print "T1u:\n"+str(T1u)
w1=(2*u*T0u)/T1u
print "w1:\n"+str(w1)

b=np.array([[3.],[3.]])
x1=np.array([[(G+la.inv(P)*b)[0,0]],[(G+la.inv(P)*b)[1,1]]])
print "x1:\n"+str(x1)
y1=x1
print "y1:\n"+str(y1)

z1=np.matrix([[(la.inv(P)*b-np.dot(np.dot(la.inv(P),A),y1))[0,0]],[(la.inv(P)*b-np.dot(np.dot(la.inv(P),A),y1))[1,1]]])
print "z1:\n"+str(z1)

w2=(2*u*T1u)/(np.polynomial.chebyshev.chebvander(u,2)[0,2])
print "w2:\n"+str(w2)

y2=y0+np.dot(w2,(y1-y0+i*z1))
print "y2:\n"+str(y2)
