''''
File: PotenciasInversas_v2.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:19|Nov|2015
Version:2.0
'''

import numpy as np
from numpy import linalg as la


A=np.matrix([[2.,-1.,0.],[-1.,2.,-1.],[0.,-1.,2.]])
#print A

print "Valores pp: ",la.eigvals(A)

x0=np.array([0.,1.,0.])

def potinv(A,x0,sigma,it):
    n=A.shape[0]
    I=np.identity(n)
    AI=(A-(sigma)*I)
    print AI
    xk=x0
    print xk
    yk=1
    vk=1
    for i in range (it):
        yk=la.solve(AI,xk)
        vk=np.inner(xk,yk)
        xk=yk/la.norm(yk,2)
    return (1/vk)+sigma

print "sigma=0.5: ",potinv(A,x0,0.5,10)
print "sigma=1.5: ",potinv(A,x0,1.5,10)
print "sigma=3.: ",potinv(A,x0,3.,10)
