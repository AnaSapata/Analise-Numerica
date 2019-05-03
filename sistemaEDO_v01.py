# -*- coding: utf-8 -*-
'''
File: sistemaEDO_v01.py
    -
Author: AnaSapata,ana_sapata@sapo.pt
Date: 10|Dez|2015
Version:0.1
'''

import numpy as np

'''
Sabemos o valor do y0 e do x0 que nos são dados no enunciado
De seguida calculamos o y1 para o qual precisamos do x0
e calculamos o x1 para o qual precisamos o y0 e assim sucessivamente

y2 - - precisamos x1
x2 - - precisasmos y2
'''

x0=1
y0=0

def fx(yk):
    return -np.pi*yk

def fy(xk):
    return np.pi*xk

t0=0
T=0.5
h=0.1

n=int((T-t0)/h)
t=[]
for i in range(n):
    t.append(round(t0+i*h,2))
print t

#x1=-np.pi*y0
x1=fx(y0)
#y1=np.pi*x0
y1=fy(x0)
print x1
print y1
