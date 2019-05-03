''''
File: MetodoPotenciasDiretas_v3.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:06|Nov|2015
Version:3.0
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[2.,1.],[1.,2.]])
x0=np.array([1.,0.])

def potdir(A,x0,tol):
    A=np.squeeze(np.asarray(A))
    xk=np.squeeze(np.asarray(x0))
    vk=1
    vkk=2
    #i=0
    while abs(vkk-vk)/abs(vk)>tol or abs(vk-vkk)/abs(vkk)==tol:
        yk=np.dot(A,xk)
        vkk=vk
        vk=np.inner(xk,yk)
        xk=yk/la.norm(yk,2)
        #i+=1
    #return vk,i
    return vk

#vk,i=potdir(A,x0,0.1)
vk=potdir(A,x0,1.e-6)
print vk
#print i
