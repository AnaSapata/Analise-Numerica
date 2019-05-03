'''
File: GramSchmidt_v2_1.py
-
Autor: AnaSapata, ana_sapata@sapo.pt
Date: 23|Out|2015
Version: 2.1
'''

import numpy as np
from numpy import linalg as la


def Gram (A):
    R=np.identity(3)
    Q=np.zeros((3,3),dtype=float)
    for i in range(3): #coluna
        wk=A[0:,i]
        for j in range(i+1): #linha
            if i==j:
                R[i,i]=la.norm(wk,2)
                q=(wk)/(la.norm((wk),2))
            else:
                #print "q1:"+str(q)
                #print "w1:"+str(wk)+"\n"
                #print np.inner(np.squeeze(np.asarray(wk)),np.squeeze(np.asarray(Q[0:,j])))
                R[j,i]=np.inner(np.squeeze(np.asarray(wk)),np.squeeze(np.asarray(Q[0:,j])))
                #print "q2:"+str(q)
                #print "w2:"+str(wk)+"\n"
                #print "OK"
                #print R[j,i]
                #print R[j,i]*q
                print wk
                print R[j,i]
                print q
                print R[j,i]*Q[0:,j]
                wk=np.squeeze(np.asarray(wk))-R[j,i]*Q[0:,j]
                print wk
                q=wk*la.norm(wk,2)
                print q
        for k in range (3):
            Q[k,i]=q[k]
    return R, Q

A=np.matrix([[2.,2.,1.],[2.,3.,2.],[1.,2.,3.]])
print Gram(A)

'''
i=0 j=(0)
i=1 j=(0,1)
i=2 j=(0,1,2)

A=np.matrix([[2.,2.,1.],[2.,3.,2.],[1.,2.,3.]])
R=np.identity(3)
Q=np.identity(3)
#print R
#print Q

#k=1
w1=a1=A[0:,0]
print w1
R[0,0]=la.norm(w1,2)
print R
q1=w1/la.norm(w1,2)
print q1

#k=2
w2=a2=A[0:,1]
#print w2
R[0,1]=np.inner(np.squeeze(np.asarray(w2)),np.squeeze(np.asarray(q1)))
#print R
w2=w2-R[0,1]*q1
#print w2
R[1,1]=la.norm(w2,2)
#print R
q2=w2*la.norm(w2,2)
#print q2

#k=3
w3=a3=A[0:,2]
#print w3
R[0,2]=np.inner(np.squeeze(np.asarray(w3)),np.squeeze(np.asarray(q1)))
#print R
w3=w3-R[0,2]*q1
#print w3
R[1,2]=np.inner(np.squeeze(np.asarray(w3)),np.squeeze(np.asarray(q2)))
#print R
w3=w3-R[1,2]*q2
#print w3
R[2,2]=la.norm(w3,2)
#print R
q3=w3*la.norm(w3,2)
#print q3

Q[:,0]=np.squeeze(np.asarray(q1))
Q[:,1]=np.squeeze(np.asarray(q2))
Q[:,2]=np.squeeze(
Q[1,2]=q3[1,0]
Q[2,2]=q3[2,0]
print "Q:\n"+str(Q)
print "R:\n"+str(R)
'''
