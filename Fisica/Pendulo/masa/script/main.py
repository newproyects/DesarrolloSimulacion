#!/bin/python3

import numpy as np
from numpy import pi,sin
import matplotlib.pyplot as plt
from vpython import *

g=9.81
t=np.array([0.0])
o=np.array([0.99*pi])
w=np.array([0.0])
r=0.1
L=5
l=L/2
m=5

#cilindro

I=(1/4)*m*r**2+(1/3)*m*L**2

v=np.array([-m*g*l*cos(o[0])])
k=np.array([0.5*I*w[0]**2])
e=np.array([k[0]+v[0]])

h=0.01

mom=(1/4)*m*r**2+(1/3)*m*L**2

for i in range(0,10000):
    t=np.append(t,t[i]+h)
    w=np.append(w,w[i]-h*m*g*l*sin(o[i])/I)
    o=np.append(o,o[i]+h*w[i+1])
    v=np.append(v,-m*g*l*cos(o[i]))
    k=np.append(k,0.5*I*w[i]**2)
    e=np.append(e,k[i]+v[i])

plt.plot(t,o)
plt.show()
plt.plot(t,k,color="red")
plt.plot(t,v,color="blue")
plt.plot(t,e,color="brown")
plt.title("Energía vs tiempo")
plt.xlabel("tiempo")
plt.ylabel("Energía")
plt.show()


#Vpython-Simulación
run=False
scene=canvas(title='Péndulo físico',center=vector(0,L,0))
def runbutton(b):
    global run
    run=not run
    if not run: b.text='Run'
    else: b.text='Pause'

b=button(text='Run',bind=runbutton)

pivot=vector(0,L,0)
s=sphere(pos=vector(0,L,0),mass=1,radius=2*r,color=color.white)
#point=sphere(pos=vector(0,0,0),mass=1,radius=l*0.07,color=color.red)
bar=cylinder(pos=pivot,axis=vector(L*sin(o[0]),-L*cos(o[0]),0),radius=r,color=color.white)

for i in range(0,10000):
    sleep(1e-5)
    while(not run):()
    #point.pos=vector(l*sin(o[i]),l-l*cos(o[i]),0)
    bar.axis=vector(L*sin(o[i]),L-L*cos(o[i]),0)-bar.pos


