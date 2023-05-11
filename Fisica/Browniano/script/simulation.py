import numpy as np

class data:
    def __init__(self,R,m,ID):
        self.r=np.zeros([m,R])
        self.v=np.zeros([m,R])
        self.ID=ID

def simul(C,k,T,R,M,h,n,m):
    
    std=np.sqrt(2*C*k*T*h)
    a=(1-h*C/M)
    b=std/m
    
    Particulas=[]

    for i in range(n):
        Particulas.append(data(R,m,i))
        #Particulas[i].r[0]=0.005*np.random.randn(R)

    for i in range(1,m):
        for j in range(n):
            Particulas[j].r[i]=Particulas[j].r[i-1]+Particulas[j].v[i-1]*h
            Particulas[j].v[i]=a*Particulas[j].v[i-1]+b*np.random.randn(R)

    return Particulas
