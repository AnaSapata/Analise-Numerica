# -*- coding: utf-8 -*-
''''
File: GradientesConjugados_v3(2).py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:07|Dez|2015
Version:3.2
'''

import numpy as np
from numpy import linalg as la

#A=np.matrix([[3.,-1.,0.],[-1.,2.,-1.],[0.,1.,1.]])
#b=np.array([1.,0.,1.])

#Na maioria das vezes constroi uma matriz com diagonal dominante, logo a matriz é definida positiva
#pelo que é possivel aplicar o metodo
def matrizes():
    #O utilizador diz o numero de linhas/colunas que pretende para a matriz
    l=input("Numero de linhas/colunas:")
    #Criação de uma matriz lxl de zeros
    A=np.zeros((l,l),dtype=float)
    #Criação de um vetor b de zeros que irá ser preenchido durante o "processo"
    b=np.zeros(l)
    #Ciclos que vão construir uma matriz simétrica em que os valores da diagonal
    #variam entre 0 e 20 de modo a que a matriz tenha diagonal dominante, uma vez
    #que os restantes valores da matriz variam apenas entre -5 e 5
    for i in range (l):
        for j in range(i,l):
            if j==i:
                A[i,j]=round(np.random.uniform(0,20),2)
            else:
                A[i,j]=A[j,i]=round(np.random.uniform(-5,5),2)
    #Construção do vetor b para a resolução do sistema Ax=b
        b[i]=round(np.random.uniform(-10,10),2)
    print "Valores proprios:\n"+str(la.eigvals(A))
    return A,b

def grad_conj(A,b,tol):
    #Tamanho da matriz A
    n=A.shape[0]
    #Criação do vetor x Com tamanho n e todas as suas componentes iguais a zero
    xk=np.zeros(n)
    rk=-b
    betak=0
    pk=b
    #O cilco só irá parar quando a norma do rk for maior que o valor da tolerancia dado pelo utilizador
    while la.norm(rk,2)>tol or la.norm(rk,2)==tol:
        #Implementação do metodo em si, calculo do tauk, xk, rk, betak, pk
        Apk=np.dot(A,pk)
        tauk=-(np.inner(pk,rk)/(np.inner(pk,Apk)))
        xk=xk+tauk*pk
        rk=np.squeeze(np.asarray(np.dot(A,xk)))-b
        betak=np.inner(rk,Apk)/np.inner(pk,Apk)
        pk=-rk-betak*pk
    #A função solve do modulo linalg dá-nos a solução exata do sistema Ax=b, em comparação
    #com o resultado que obtemos(xk) conseguimos calcular o erro
    erro=(la.solve(A,b))-xk
    return xk,erro

A,b=matrizes()
#print A
#print b
x,erro=grad_conj(A,b,1.e-5)
print "exata:"+str(la.solve(A,b))
print "gradiente conjugado:"+str(x)
print "erro:"+str(erro)
#grad_conj(A,b,1.e-5)
