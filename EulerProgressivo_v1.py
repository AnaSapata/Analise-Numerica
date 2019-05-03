'''
File: EulerProgressivo_v1.py
    -
Author: AnaSapata,ana_sapata@sapo.pt
Date: 13|Nov|2015
Version:1.0
'''

import numpy as np
import sympy as sy
from sympy import *

'''
t=symbols('t')
u=symbols('u')
du_dt=t*u
print du_dt
print du_dt.subs(5,4)
'''
def f(t,u):
    return t*u

u0=2
h=0.25
t=[0,0.25,0.5,0.75,1.]
y0=u0
print "y0="+str(y0)

y1=y0+h*f(t[0],y0)
print "y1="+str(y1)

y2=y1+h*f(t[1],y1)
print "y2="+str(y2)

y3=y2+h*f(t[2],y2)
print "y3="+str(y3)

y4=y3+h*f(t[3],y3)
print "t4="+str(y4)
