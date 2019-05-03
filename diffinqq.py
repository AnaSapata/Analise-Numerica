'''
def diffin(t0,T,h,alfa,beta):
    n=int((T-t0)/h)
    print n
    A=np.zeros((n,n),dtype=float)
    print A
    b=np.zeros((n,1),dtype=float)
    print b
    for k in range(1,n):
        ai,bi,ci,di=coef(k,h)
        pi=-ci*h**2+2*ai
        qi=-ai-0.5*bi*h
        ri=-ai+0.5*bi*h
        if k==0:
            A[k,k]=pi
            A[k,k+1]=qi
            b[k,0]=-h**2(di+(ri/h**2)*alfa)
        if k==(n-1):
            A[k,k]=pi
            A[k,k-1]=ri
            b[k,0]=-h**2(di+(qi/h**2)*beta)
        else:
            A[k,k-1]=ri
            A[k,k]=pi
            A[k,k+1]=qi
            b[k,0]=-h**2(di)
    return A,b

t0=0
T=1
h=0.25
alfa=0
beta=1

A,b=diffin(t0,T,h,alfa,beta)
print A
print b
'''
