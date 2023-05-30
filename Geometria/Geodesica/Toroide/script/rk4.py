import numpy as np

def step(y,f,h):
    k1=f(y)
    k2=f(y+0.5*h*k1)
    k3=f(y+0.5*h*k2)
    k4=f(y+h*k3)

    return y+(h/6)*(k1+2*k2+2*k3+k4)

def run(y,f,h,n):
    v=np.array(n*[y])
    for i in range(n-1):
        #print(v[i+1])
        v[i+1]=step(v[i],f,h)

    return v
