import matplotlib.pyplot as plt
import numpy as np
from numpy import pi,cos,sin
from rk4 import run
from graph import graph

def f(y):
    d1=-(1/r)*(R+r*cos(y[0]))*sin(y[0])*y[3]**2
    d2=(1/(R+r*cos(y[0])))*r*sin(y[0])*y[1]*y[3]
    return np.array([y[1],d1,y[3],d2])

R=4
r=2

h=0.01
T=10
n=int(T/h)

m=20
a=np.linspace(0.48,0.5,m)
b=np.linspace(0.18,0.2,m)

aa=1
bb=1

P1=np.array([pi/2,0])
P2=np.array([3*pi/2,pi])

var=np.array([])

y=0
for i in range(m):
    for j in range(m):
        v=np.array([P1[0],a[i],P1[1],b[j]])
        v=run(v,f,h,n)
        var=np.append(var,np.linalg.norm(P2-np.array([v[-1,0],v[-1,2]])))
        if var[-1]<=var.min():
            y=v
            aa=a[i]
            bb=b[j]

print(f'aa:{aa} , bb:{bb}')
print(f'varmin:{var.min()}')

u1=np.array([])
u2=np.array([])
for i in range(n):
    u1=np.append(u1,y[i][0])
    u2=np.append(u2,y[i][2])


graph(u1,u2,P1,P2,R,r)
