# -*- coding: utf-8 -*-
''''
File: PotenciasCombinadas_v2(1).py
    -Implementação do metodo das potencias combinadas, de modo a dada uma matriz A
        saber-se qual o seu valor proprio com maior modulo e o respetivo vetor proprio
    -O ficheiro é composto por 2 funções:
    - matrizes: constroi uma matriz A nxn com os seus coeficientes entre -10 e 10
        e um vetor x0 de norma igual a 1
    - potcomb: dada uma matriz A, um vetor inicial x0 e uma determinada tolerância
        é efetuado algumas vezes o metodo das potencias diretas de modo a obter-se
        uma aproximação do vetor proprio para o valor proprio com maior valor absoluto
        e de sguida é efetuado o metodo das potencia inversas com sigma igual ao
        quociente de Rayleigh no qusl é utilizado a respetiva aproximação do vetor
        proprio obtida anteriormente, o metodo retorna então valor proprio com
        maior valor absoluto
Author: AnaSapata, ana_sapata@sapo.pt
Date:19|Nov|2015
Version:2.1
'''

import numpy as np
from numpy import linalg as la

#Constroi uma matriz A lxl simétrica, uma vez que as matrizes não simetricas têm
#valores proprios complexos
def matrizes():
    #Pede ao utilizador a dimensão da matriz
    l=input("Numero de linhas\colunas:")
    #Constroi uma matriz lxl com os coeficientes iguais a zero
    A=np.zeros((l,l),dtype=float)
    #Ciclo que determina os coeficientes da matriz de modo a esta ser simétrica
    for i in range (l):
        for j in range(i,l):
            A[i,j]=A[j,i]=round(np.random.uniform(-10,10),2)
    #Construção do vetor x0 com norma igual a 1
    x0=np.zeros(l)
    x0[0]=1
    return A,x0

#Implementação do metodo das potencias combinado
def potcom(A,x0,tol):
    #Passagem da matriz para array
    A=np.squeeze(np.asarray(A))
    #Dimensão da matriz
    n=A.shape[0]
    #Criação da matriz identidade de dimensão nxn
    I=np.identity(n)
    #Passagem do vetor x0 a array
    xk=np.squeeze(np.asarray(x0))
    #Inicialização do valor v e do valor y, sendo no fim vk uma aproximação do
    #valor proprio com maior valor absoluto
    yk=1
    vk=1
    #Implementação do metodo das Potencias Diretas
    for i in range(20):
        yk=np.dot(A,xk)
        vk=np.inner(xk,yk)
        xk=yk/la.norm(yk,2)
    #Calculo do quociente de Rayleigh
    sigma=(np.inner(xk,np.dot(A,xk)))/(np.inner(xk,xk))
    #Calculo da matriz A-sigma*I
    AI=(A-(sigma)*I)
    c=1
    #Ciclo que implementa o metodo das potencias inversas com sigma igual ao
    #quociente de Rayleigh, parando quando c for maior ou igual que a tolerancia
    #dada
    while c>tol:
        yk=la.solve(AI,xk)
        vk=np.inner(xk,yk)
        xk=yk/la.norm(yk,2)
        sigmak=(np.inner(xk,np.dot(A,xk)))/(np.inner(xk,xk))
        c=(abs(sigmak-sigma))/abs(sigma)
        sigma=sigmak
    #uma vez que o metodo das potencias inversas dá 1/(lamba -sigma), onde lambda
    #é o valor proprio da matriz A com maior valor absoluto se dividirmos 1 por
    #este valor e adicionarmos sigma iremos obter o lambda
    return (1/vk)+sigma

print "\n\t Implementação do Método das Potências Combinadas"

A,x0=matrizes()

print "\n Valores próprios exatos de A: \n",la.eigvals(A)
print "\n Valor próprio obtido pelo método: \n",potcom(A,x0,1.e-20)
