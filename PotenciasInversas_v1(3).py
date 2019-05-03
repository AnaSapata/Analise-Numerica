''''
File: PotenciasInversas_v1(3).py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:19|Nov|2015
Version:1.3
'''

import numpy as np
from numpy import linalg as la

#SIGMA=0.5

A=np.matrix([[2.,-1.,0.],[-1.,2.,-1.],[0.,-1.,2.]])
#print A

print "Valores pp: ",la.eigvals(A)

n=A.shape[0]
I=np.identity(n)
#print I

#print (A-0.5*I)

x0=np.array([0.,1.,0.])

AI=(A-3*I)

y1=la.solve(AI,x0)
print "y1: ",y1

v1=np.inner(x0,y1)
print "v1: ",v1

x1=y1/la.norm(y1,2)
print "x1: ",x1

#x12=np.array([(5*np.sqrt(77))/77,(6*np.sqrt(77))/77,(4*np.sqrt(77))/77])
#print "x12: ", x12

y2=la.solve(AI,x1)
print "y2: ",y2

v2=np.inner(x1,y2)
print "v2: ",v2

x2=y2/la.norm(y2,2)
print "x2: ",x2

y3=la.solve(AI,x2)
print "y3: ",y3

v3=np.inner(x2,y3)
print "v3: ",v3

x3=y3/la.norm(y3,2)
print "x3: ",x3

y4=la.solve(AI,x3)
print "y4: ",y4

v4=np.inner(x3,y4)
print "v4: ",v4

x4=y4/la.norm(y4,2)
print "x4: ",x4

y5=la.solve(AI,x4)
print "y5: ",y5

v5=np.inner(x4,y5)
print "v5: ",v5

x5=y5/la.norm(y5,2)
print "x5: ",x5

y6=la.solve(AI,x5)
print "y6: ",y5

v6=np.inner(x5,y6)
print "v6: ",v6

x6=y6/la.norm(y6,2)
print "x6: ",x6

print (1/v6)+3
