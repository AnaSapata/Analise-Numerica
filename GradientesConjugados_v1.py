''''
File: GradientesConjugados_v1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:06|Nov|2015
Version:1.0
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[3.,-1.,0.],[-1.,2.,-1.],[0.,1.,1.]])
b=np.array([1.,0.,1.])

#k=0
x0=np.array([0.,0.,0.])
print "x0:\n"+str(x0)
r0=-b
print "r0:\n"+str(r0)
beta0=0
print "Beta0:\n"+str(beta0)
p1=b
print "p1:\n"+str(p1)

#k=1
Ap1=np.dot(A,p1)
print "A*p1:\n"+str(Ap1)
#print np.inner(p1,r0)
#print np.inner(p1,Ap1)[0]
tau1=-(np.inner(p1,r0)/(np.inner(p1,Ap1)[0]))
print "tau1:\n"+str(tau1)
x1=x0+tau1*p1
print "x1:\n"+str(x1)
r1=np.squeeze(np.asarray(np.dot(A,x1)))-b
print "r1:\n"+str(r1)
beta1=np.inner(r1,Ap1)/np.inner(p1,Ap1)
print "Beta1:\n"+str(beta1)
p2=-r1-beta1*p1
print "p2:\n"+str(p2)

#k=2
Ap2=np.dot(A,p2)
print "A*p2:\n"+str(Ap2)
tau2=-(np.inner(p2,r1)/(np.inner(p2,Ap2)[0]))
print "tau2:\n"+str(tau2)
x2=x1+tau2*p2
print "x2:\n"+str(x2)
r2=np.squeeze(np.asarray(np.dot(A,x2)))-b
print "r2:\n"+str(r2)
beta2=np.inner(r2,Ap2)/np.inner(p2,Ap2)
print "Beta2:\n"+str(beta2)
p3=-r2-beta2*p2
print "p3:\n"+str(p3)

#k=3
Ap3=np.dot(A,p3)
print "A*p3:\n"+str(Ap3)
tau3=-(np.inner(p3,r2)/(np.inner(p3,Ap3)[0]))
print "tau3:\n"+str(tau3)
x3=x2+tau3*p3
print "x3:\n"+str(x3)
r3=np.squeeze(np.asarray(np.dot(A,x3)))-b
print "r3:\n"+str(r3)
beta3=np.inner(r3,Ap3)/np.inner(p3,Ap3)
print "Beta3:\n"+str(beta3)
p4=-r3+beta3*p3
print "p4:\n"+str(p4)
