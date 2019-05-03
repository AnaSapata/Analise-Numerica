'''
File: EulerProgressivo_v2.py
    -
Author: AnaSapata,ana_sapata@sapo.pt
Date: 13|Nov|2015
Version:2.0
'''

import numpy as np
import sympy as sy
from sympy import *

def f(t,u):
    return t*u

def EulerProg(u0,h,iin,ifi):
    yk=u0
    n=int((ifi-iin)/h)
    t=[iin]
    for i in range(n):
        t.append(t[i]+h)
    for j in range(n):
        yk=yk+h*f(t[j],yk)
    return yk


u0=2
h=0.25
print EulerProg(u0,h,0.,1.)
