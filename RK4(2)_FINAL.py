# -*- coding: utf-8 -*-
''''
File: RK4(2)_FINAL.py
    - O ficheiro é composto apenas por uma função sendo esta a RK42, que é a implementação
        do metodo RK4/2 que serve para resolver EDO's. A função tem como parametros
        o valor inicial e final do intervalo a utilizar, bem como o valor de u associado a t0
        e o passo utilizado
    - O programa calcula a solução para a EDO por este metodo, mostrando no fim, um grafico
        com a solução por este metodo, a solução exata e o erro
Author: AnaSapata, ana_sapata@sapo.pt
Date:8|Dez|2015
Version:2.0
'''

import numpy as np
import matplotlib.pyplot as plt
import funcao1 as fc

#Função que implementa o metodo RK4/2, para tal recebe como argumentos t0 e T, que são o
#valor inicial e valor final, respetivamente, do intervalo que é utilizado, o passo h,
#e u0 que é o valor de u para x=t0
def RK42(t0,T,h,u0):
    #Construção do array y que será a solução do problema, tendo como valor inicial o u0
    y=[u0]
    #Calculo do numero de nós
    n=(T-t0)/h
    #Inicialização do valor de t, que serão o x0,x1,...,xn
    t=t0
    #Ciclo que calculará os valores de F1, F2, F3, F4 e yk, adicionando este ultimo
    #ao array y construido anteriormente que será a solução
    for i in range(int(n)):
        F1=fc.f(t,y[i])
        F2=fc.f(t+0.25*h,y[i]+0.25*h*F1)
        F3=fc.f(t+0.5*h,y[i]+0.5*h*F2)
        F4=fc.f(t+h,y[i]+h*F1-2*h*F2+2*h*F3)
        yk=y[i]+(h/6)*(F1+4*F3+F4)
        y.append(yk)
        t+=h
    return y

#Calculo da solução através do metodo RK4/2
sol=RK42(fc.t0,fc.T,fc.h,fc.u0)

#Calculo do numero de nós da malha
N=int((fc.T-fc.t0)/fc.h)+1

#Criação da malha
r=np.linspace(fc.t0,fc.T,num=N)

#Calculo da solução exaTa
s=fc.exata(r)

#Calculo do erro
erro=s-sol

print "Solução exata:\n"+str(r)
print "Solução pelo metodo RK4/2:\n"+str(sol)
print "Erro:\n"+str(erro)

#Criação do "grafico"
ax=plt.axes()
ax.grid(True)

#Especificação do tipo de letra a usar
plt.rc('text',usetex=False)
plt.rc('font',family='serif')

#Representação da solução pelo metodo RK4/2 no gráfico, sendo a sua ilustração feita
#por pequenos circulos amarelos
plt.plot(r,sol,'yo',label='Approximated solution')

#Representação da solução exata no gráfico, sendo a sua ilustração atraves de uma linha vermelha
plt.plot(r,s,'r', label='Exact solution')

#Representação do erro no gráfico, sendo a sua ilustração feita por uma linha '- - - ' em preto
plt.plot(r,erro,'k_', label='Error')

#Definição do maximo e minimo para cada eixo
plt.axis([0.,6.,-50.,50])

#Definição da variavel representada pelo eixo dos xx
plt.xlabel(r'time(s)',fontsize=16)

#Definição do nome do gráfico
plt.title(r"RK4/2", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)

#Definição das legendas
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

#Mostrar o grafico
plt.show()
