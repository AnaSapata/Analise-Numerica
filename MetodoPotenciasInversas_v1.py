''''
File: MetodoPotenciasInversas_v1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:19|Nov|2015
Version:1.0
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[2.,1.,0.],[2.,5.,3.],[0.,1.,6.]])
x0=np.array([1.,1.,1.])

#A=np.squeeze(np.asarray(A))
#xk=np.squeeze(np.asarray(x0))

y1=la.solve(A,x0)
print y1

alfa1=max(abs(y1))
print alfa1

x1=y1/alfa1
print x1

y2=la.solve(A,x1)
print y2

v1=la.norm(y2,2)/la.norm(x1,2)
print v1

alfa2=max(abs(y2))
print alfa2

x2=y2/alfa2
print x2

y3=la.solve(A,x2)
print y3

v2=la.norm(y3,2)/la.norm(x2,2)
print v2

alfa3=max(abs(y3))
print alfa3

x3=y3/alfa3
print x3

y4=la.solve(A,x3)
print y4

v3=la.norm(y4,2)/la.norm(x3,2)
print v3

alfa4=max(abs(y4))
print alfa4

x4=y4/alfa4
print x4

y5=la.solve(A,x4)
print y5

v4=la.norm(y5,2)/la.norm(x4,2)
print v4
print 1/v4
print la.eigvals(A)
