# -*- coding: utf-8 -*-
''''
File: tiro_v4dpsdafinal.py
    -O programa resolve EDO's de segunda ordem através do metodo do tiro, para tal
        o ficheiro está composto por varias funções sendo elas:
    - fy, fw - que são as funções definem os PVI para podermos resolver a
        EDO de segunda ordem
    - exata - que dá a solução exata da EDO
    - RK42 - que utiliza o metodo RK4/2 para resolver os dois PVI's
    - final - que através da resolução dos PVI's pelo metodo RK4/2, calcula a solução
        da EDO de segunda ordem
Author: AnaSapata, ana_sapata@sapo.pt
Date:16|Dez|2015
Version:4.0
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as s
from scipy import stats

#definição da função y' do PVI
def fy(tk,yk,wk):
    return wk

#definição da função w' tanto para o PVI1 como para o PVI2, daí o uso da variavel b
def fw(tk,yk,wk,b):
    if b==1:
        return (-2./tk)*wk+(2/(tk**2))*yk+np.sin(np.log(tk))/(tk**2)
    else:
        return (-2./tk)*wk+(2/(tk**2))*yk

#definição da função que nos dá a solução exata
def exata(t0,T,h):
    n=int((T-t0)/h)+1
    y=np.zeros(n)
    for i in range(n):
        t=t0+i*h
        c2=1./70.*(8-12*np.sin(np.log(2))-4*np.cos(np.log(2)))
        c1=11./10.-c2
        yk=c1*t+c2/(t**2)-3./10.*np.sin(np.log(t))-1./10.*np.cos(np.log(t))
        y[i]=yk
    return y

#adaptação do metodo RK4/2, implementado anteriormente, aos problemas de valor iniciar
def RK42(y0,w0,h,t0,T,b):
    n=int((T-t0)/h)
    y=np.zeros(n+1)
    w=np.zeros(n+1)
    y[0]=y0
    w[0]=w0
    for i in range(n):
        t=t0+i*h
        F1y=fy(t,y[i],w[i])
        F1w=fw(t,y[i],w[i],b)
        F2y=fy(t+0.25*h,y[i]+0.25*h*F1y,w[i]+0.25*h*F1w)
        F2w=fw(t+0.25*h,y[i]+0.25*h*F1y,w[i]+0.25*h*F1w,b)
        F3y=fy(t+0.5*h,y[i]+0.5*h*F2y,w[i]+0.5*h*F2w)
        F3w=fw(t+0.5*h,y[i]+0.5*h*F2y,w[i]+0.5*h*F2w,b)
        F4y=fy(t+h,y[i]+h*F1y-2*h*F2y+2*h*F3y,w[i]+h*F1w-2*h*F2w+2*h*F3w)
        F4w=fw(t+h,y[i]+h*F1y-2*h*F2y+2*h*F3y,w[i]+h*F1w-2*h*F2w+2*h*F3w,b)
        y[i+1]=y[i]+(h/6)*(F1y+4*F3y+F4y)
        w[i+1]=w[i]+(h/6)*(F1w+4*F3w+F4w)
    return y,w

#determinação da solução da EDO de segunda ordem, está é construida através das
#soluções para a variavel y dos PVI's e de uma constante que é formada pelo beta,
#ou seja, o valor de y do ultimo xk(tk) e pelas soluções dos PVI's no ultimo
#nó da malha utilizada
def final(y1,y2,t0,T,h,beta):
    n=int((T-t0)/h)
    y=np.zeros(n+1)
    c=(beta-y1[n])/y2[n]
    for i in range(n+1):
        y[i]=y1[i]+c*y2[i]
    return y
#Valor inicial do intervalo
t0=1
#Valor final do intervalo
T=2
#Passo a utilizar
h=0.25/16
#Valores no nó t0 da malha para as funções y e w(1 e 2)
y01=1
w01=0
y02=0
w02=1

#Valores obtidos pelo metodo RK4/2 para o PVI1 e o PVI2
y1,w1=RK42(y01,w01,h,t0,T,1)
y2,w2=RK42(y02,w02,h,t0,T,2)

#Solução final do PVF
yt=final(y1,y2,t0,T,h,2)

#Solução exata do PVF
ye=exata(t0,T,h)

#Erro da solução ao ser calculado pelo metodo RK4/2
erro=ye-yt

print "Solução pelo metodo do tiro:\n"+str(yt)
print "Solução exata:\n"+str(ye)
print "Erro:\n"+str(erro)
N=int((T-t0)/h)+1

r=np.linspace(t0,T,num=N)

#Como só temos uma variavel independente a reta de regressão vai ser do tipo y=b+mx
#através da função linregress do modulo stats conseguimos saber o declive(m) da
#reta de regressão e o ponto em que esta interseta o eixo dos yy (b)
m, b, r_value, p_value, std_err = stats.linregress(r,erro)
#Função que calcula os valores da reta de regressão nos nós da malha
def regressao(m,x,b):
    return m*x+b

#definição da reta de regressão
reg=regressao(m,r,b)

#representação gráfica da solução exata e da solução aproximada pelo metodo do tiro,
#representadas por uma linha vermelha e pontos vermelhos, respetivamente
plt.figure(1)
ax=plt.axes()
ax.grid(True)
plt.rc('text',usetex=False)
plt.rc('font',family='serif')
plt.plot(r,yt,'r.',label='Approximated solution')
plt.plot(r,ye,'r', label='Exact solution')
plt.axis([0.95,2.05,0.95,2.05])
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"Metodo do tiro", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

#representação gráfica da solução exata e da solução aproximada pelo metodo do tiro,
#representadas por uma linha vermelha e pontos vermelhos, respetivamente
plt.figure(2)
ax=plt.axes()
ax.grid(True)
plt.rc('text',usetex=False)
plt.rc('font',family='serif')
plt.plot(r,erro,'r.',label='Error')
plt.plot(r,reg,'r', label='Regression Line')
plt.axis([0.95,2.05,-1.e-10,4.e-10])
plt.xlabel(r'time(s)',fontsize=16)
plt.title(r"Metodo do tiro", fontsize=20,color='blue',y=1.08)
plt.subplots_adjust(top=0.8)
legend=plt.legend(loc='upper center',prop={'size':14}, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#C0F9E2')

plt.show()
