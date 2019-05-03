'''
File:Trapezio_v1.py
    -
Author: AnaSapata,ana_sapata@sapo.pt
Date:13|Nov|2015
Version:1.0
'''

def f(t,u):
    return t*u

u0=2
h=0.25
t=[0.,0.25,0.50,0.75,1.]

y0=u0
print "y0="+str(y0)

y1=(2*y0+h*t[0]*y0)/(2-h*t[1])
print "y1="+str(y1)

y2=(2*y1+h*f(t[1],y1))/(2-h*t[2])
print "y2="+str(y2)

y3=(2*y2+h*f(t[2],y2))/(2-h*t[3])
print "y3="+str(y3)

y4=(2*y3+h*f(t[3],y3))/(2-h*t[4])
print "y4="+str(y4)
