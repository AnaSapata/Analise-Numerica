''''
File: PotenciasCombinadas_v1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:19|Nov|2015
Version:1.0
'''

import numpy as np
from numpy import linalg as la


#A=np.array([[2.,-1.,0.],[-1.,2.,-1.],[0.,-1.,2.]])
#A=np.array([[2.,1.,0],[1.,-2.,1.],[0.,1.,2.]])
A=np.array([[5.,1.,0.],[1.,5.,2.],[0.,2.,5.]])
#print A

print "Valores pp: ",la.eigvals(A)

x0=np.array([0.,1.,0.])

def potdir(A,x0,it):
    xk=x0
    yk=1
    vk=1
    for i in range(it):
        yk=np.dot(A,xk)
        vk=np.inner(xk,yk)
        xk=yk/la.norm(yk,2)
    return vk,xk

def potinv(A,x0,it):
    n=A.shape[0]
    I=np.identity(n)
    xk=x0
    sigma=(np.inner(xk,np.dot(A,xk)))/(np.inner(xk,xk))
    AI=(A-(sigma)*I)
    yk=1
    vk=1
    for i in range (it):
        yk=la.solve(AI,xk)
        vk=np.inner(xk,yk)
        xk=yk/la.norm(yk,2)
        sigma=(np.inner(xk,np.dot(A,xk)))/(np.inner(xk,xk))
    return (1/vk)+sigma


vk,xk=potdir(A,x0,3)
print "valor proprio:",vk

print "sigma=quociente de Rayleigh:",potinv(A,xk,20)
