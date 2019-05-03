''''
File: MetodoPotenciasDiretas_v2.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:06|Nov|2015
Version:2.0
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[2.,1.],[1.,2.]])
x0=np.array([1.,0.])

def potdir(A,x0,it):
    A=np.squeeze(np.asarray(A))
    xk=np.squeeze(np.asarray(x0))
    #vk=1
    #vkk=1
    #i=0
    #while abs(vk-vkk)/abs(vkk)>tol or abs(vk-vkk)/abs(vkk)==tol:
    for i in range(it):
        yk=np.dot(A,xk)
        #vkk=vk
        vk=np.inner(xk,yk)
        xk=yk/la.norm(yk,2)
        #i+=1
    return vk

print potdir(A,x0,3)
