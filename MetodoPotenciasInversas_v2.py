''''
File: MetodoPotenciasInversas_v2.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:19|Nov|2015
Version:2.0
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[2.,1.,0.],[2.,5.,3.],[0.,1.,6.]])
x0=np.array([1.,1.,1.])

def potinv(A,x0,it):
    A=np.squeeze(np.asarray(A))
    xk=np.squeeze(np.asarray(x0))
    vk=0
    for i in range (it):
        yk=la.solve(A,xk)
        vk=la.norm(yk,2)/la.norm(xk,2)
        xk=yk/la.norm(yk,2)
    return vk

vk=potinv(A,x0,10)
print vk
print 1/vk
print la.eigvals(A)
