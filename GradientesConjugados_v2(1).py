''''
File: GradientesConjugados_v2(1).py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:06|Nov|2015
Version:2.1
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[3.,-1.,0.],[-1.,2.,-1.],[0.,1.,1.]])
b=np.array([1.,0.,1.])

def grad_conj(A,b,tol):
    print b
    xk=np.array([0.,0.,0.])
    rk=-b
    print rk
    betak=0
    pk=b
    print pk
    j=0
    while la.norm(rk,2)>tol or la.norm(rk,2)==tol:
        j+=1
        Apk=np.dot(A,pk)
        print "Apk:\n"+str(Apk)
        tauk=-(np.inner(pk,rk)/(np.inner(pk,Apk)[0]))
        print "tauk:\n"+str(tauk)
        xk=xk+tauk*pk
        print "xk:\n"+str(xk)
        rk=np.squeeze(np.asarray(np.dot(A,xk)))-b
        print "rk:\n"+str(rk)
        betak=np.inner(rk,Apk)/np.inner(pk,Apk)
        print "betak:\n"+str(betak)
        pk=-rk-betak*pk
        print "pk:\n"+str(pk)
    return xk

print grad_conj(A,b,1.e-5)
#print grad_conj(A,b,5)

print "exata:"+str(la.solve(A,b))
