''''
File: MetodoPotenciasInversas_v2(1).py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:19|Nov|2015
Version:2.1
'''

import numpy as np
from numpy import linalg as la

#A=np.matrix([[2.,1.,0.],[2.,5.,3.],[0.,1.,6.]])
#A=np.matrix([[2.,0.,0.],[0.,1.,0.],[0.,0.,1.5]])
#A=np.matrix([[2.,0.1,0.1],[0.1,1.,0.1],[0.,0.1,1.5]])
#A=np.matrix([[2.,-1.,0.],[-1.,2.,-1.],[0.,-1.,2.]])
#A=np.matrix([[2.,1.,0.],[1.,-2.,1.],[0.,1.,2.]])

x0=np.array([1.,1.,1.])

def potinv(A,sigma,x0,tol):
    n=A.shape[0]
    I=np.identity(n)
    A=np.squeeze(np.asarray(A))
    xk=np.squeeze(np.asarray(x0))
    vk=1
    vkk=2
    while abs(vkk-vk)/abs(vk)>tol or abs(vk-vkk)/abs(vkk)==tol:
        yk=la.solve((A-sigma*I),xk)
        vkk=vk
        vk=la.norm(yk,2)/la.norm(xk,2)
        xk=yk/la.norm(yk,2)
    return (1/vk)+sigma

vk=potinv(A,0.5,x0,1.e-6)
print vk
print la.eigvals(A)
