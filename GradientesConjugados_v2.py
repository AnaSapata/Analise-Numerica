''''
File: GradientesConjugados_v2.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:06|Nov|2015
Version:2.0
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[3.,-1.,0.],[-1.,2.,-1.],[0.,1.,1.]])
b=np.array([1.,0.,1.])

def grad_conj(A,b,it):
    xk=np.array([0.,0.,0.])
    rk=-b
    betak=0
    pk=b
    i=0
    for i in range(it):
        i+=1
        Apk=np.dot(A,pk)
        print "Ap"+str(i)+":\n"+str(Apk)
        tauk=-(np.inner(pk,rk)/(np.inner(pk,Apk)[0]))
        print "tau"+str(i)+":\n"+str(tauk)
        xk=xk+tauk*pk
        print "x"+str(i)+":\n"+str(xk)
        rk=np.squeeze(np.asarray(np.dot(A,xk)))-b
        print "r"+str(i)+":\n"+str(rk)
        betak=np.inner(rk,Apk)/np.inner(pk,Apk)
        print "beta"+str(i)+":\n"+str(betak)
        print "pk:\n"+str(pk)
        pk=-rk-betak*pk
        print "p"+str(i+1)+":\n"+str(pk)
    return xk

print grad_conj(A,b,3)
print grad_conj(A,b,5)

print "exata:"+str(la.solve(A,b))
