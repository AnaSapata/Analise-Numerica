''''
File: MetodoPotenciasDiretas_v1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:06|Nov|2015
Version:1.0
'''

import numpy as np
from numpy import linalg as la

A=np.array([[2.,1.],[1.,2.]])
x0=np.array([1.,0.])

y1=np.dot(A,x0)
print "y1:\n"+str(y1)

vpp1=np.inner(x0,y1)
print "valor proprio (1):\n"+str(vpp1)

x1=y1/la.norm(y1,2)
print "x1:\n"+str(x1)

y2=np.dot(A,x1)
print "y2:\n"+str(y2)

vpp2=np.inner(x1,y2)
print "valor proprio (2):\n"+str(vpp2)

x2=y2/la.norm(y2,2)
print "x2:\n"+str(x2)

y3=np.dot(A,x2)
print "y3:\n"+str(y3)

vpp3=np.inner(x2,y3)
print "valor proprio (3):\n"+str(vpp3)

x3=y3/la.norm(y3,2)
print "x3:\n"+str(x3)
