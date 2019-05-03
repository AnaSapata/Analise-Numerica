# -*- coding: utf-8 -*-
''''
File: funcao1.py
    -Ficheiro que contem uma função exata e uma função f, que é a função utilizada
        para calcular aproximadamente a solução da EDO dada na função exata
Author: AnaSapata, ana_sapata@sapo.pt
Date:2|Dez|2015
Version:1.0
'''

import numpy as np

def f(t,u):
    return (t-3.2)*u+8.*t*np.exp(0.5*((t-3.2)**2))*np.cos(4*t**2)

def exata(t):
    return np.exp(0.5*(t-3.2)**2)*np.sin(4.*t**2)

t0=0
T=6
#u0=2
u0=0
h=0.25/16
