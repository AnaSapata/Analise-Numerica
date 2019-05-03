# -*- coding: utf-8 -*-
''''
File: GradientesConjugados_v4.py
-
Author: AnaSapata, ana_sapata@sapo.pt
Date:08|Dez|2015
Version:4.0
'''

import numpy as np
from numpy import linalg as la

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
                A[i,j]=round(np.random.uniform(5,20),2)
            else:
                A[i,j]=A[j,i]=round(np.random.uniform(-5,5),2)
    #Construção do vetor b para a resolução do sistema Ax=b
        b[i]=round(np.random.uniform(-10,10),2)

    return A,b

#Verifica se a matriz A dada pela função matrizes é definida positiva ou não
#retornando False no caso de não ser e True no caso de o ser
def defpos(A):
    positiva=False
    p=[]
    #Ciclo que verifica se os valores proprios são negativos ou positivos
    #adicionando True ao array p se for positivo e False se for negativo
    for k in range(len(la.eigvals(A))):
            if la.eigvals(A)[k]<0:
                p.append(False)
            else:
                p.append(True)
    #Se o array p conter o booleano False então não é definida positiva pelo que
    #a variavel positiva vai ser igual a False caso contrario será igual a True
    if False in p:
        positiva=False
    else:
        positiva=True
    return positiva

#Implementação do metodo dos gradientes conjugados
def grad_conj(A,b,tol):
    #A variavel p dirá se a matriz é definida positiva ou não, se não o for a função
    #diz-nos que não o é e que o metodo não pode ser aplicado, no caso contrario
    #implementa o metodo
    p=defpos(A)
    if p==False:
        xk=erro="A matriz não é definida positiva pelo que não se pode aplicar o metodo"
        return xk,erro
    else:
        #Tamanho da matriz A
        n=A.shape[0]
        #Criação do vetor x Com tamanho n e todas as suas componentes iguais a zero
        xk=np.zeros(n)
        #Criação do vetor rk
        rk=-b
        #Criação da variavel betak
        betak=0
        #Criação do vetor pk
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

#Pede-se à função matrizes que construa a matriz A e o vetor b
A,b=matrizes()
#O x e o erro são dados pela função grad_conj
x,erro=grad_conj(A,b,1.e-5)
#Se o x e o erro forem strings significa que a função grad_conj está a retornar
#uma mensagem em como o metodo não pode ser aplicado devido ao facto da função
#não ser definida positiva e mostra essa mensagem, caso contrário são mostrados os
#valores proprios da matriz A para se verificar que é definida positiva, a solução
#exata, a solução pelo metodo dos gradientes conjugados e o erro
if type(x)==str and type(erro)==str:
    print x
else:
    print "Valores Próprios:\n"+str(la.eigvals(A))
    print "Solução exata:\n"+str(la.solve(A,b))
    print "Solução  pelo metodo dos gradientes conjugados:\n"+str(x)
    print "Erro:\n"+str(erro)
