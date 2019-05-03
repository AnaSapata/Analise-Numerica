'''
Title: PotenciasDiretas_v1.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 29|Out|2015
Version: 1.0
'''

import numpy as np
from numpy import linalg as la

A=np.matrix([[2.,-1.,0.],[-1.,2.,-1.],[0.,-1.,2.]])
va,ve=la.eig(A)
print va
print np.matrix.round(ve,2)
