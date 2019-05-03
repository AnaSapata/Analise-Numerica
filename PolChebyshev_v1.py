'''
File: PolChebyshev_v1.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 05|Nov|2015
Version: 1.0
'''

import numpy as np
import sympy as sy
from sympy import *
'''
x=symbols('x')
T1=x
T2=2*x**2-1

T3=2*x*T2-T1
print simplify(T3)

T4=2*x*T3-T2
print simplify(T4)
'''

def polche(v,g):
    x=symbols('x')
    pol=[x,2*x**2-1]
    for i in range(3,g+1):
        n=len(pol)
        Tk=simplify(2*x*pol[n-1]-pol[n-2])
        pol.append(Tk)
    return pol[g-1].subs(x,v)

#def pol(v,g):
 #   p=polche(g)
  #  return p.subs(x,v)

print polche(2,1)
print polche(2,2)
print polche(2,3)
print polche(2,4)

'''
print polche(1)
print polche(2)
print polche(3)
print polche(4)
print polche(5)
print polche(6)
print polche(7)
'''
