'''
File:Trapezio_v2.py
    -
Author: AnaSapata,ana_sapata@sapo.pt
Date:13|Nov|2015
Version:2.0
'''

def f(t,u):
    return t*u

def Trap(u0,h,iin,ifi,f):
    yk=u0
    n=int((ifi-iin)/h)
    t=[iin]
    print"y0="+str(u0)
    for i in range(n):
        t.append(t[i]+h)
        yk=(2*yk+h*f(t[i],yk))/(2-h*t[i+1])
        print "y"+str(i+1)+"="+str(yk)
    return ""

u0=2
h=0.25
print Trap(u0,h,0,1,f)
