''''
File: PreditorCorretor_v1.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:26|Nov|2015
Version:1.0
'''
#Fazer o calculo do erro
import numpy as np
from numpy import linalg as la

def f(t,u):
    return (t-3.2)*u+8.*t*np.exp(0.5*((t-3.2)**2))*np.cos(4*t**2)

def exata(t):
    return np.exp(0.5*(t-3.2)**2)*np.sin(4.*t**2)

def PredCorr():
