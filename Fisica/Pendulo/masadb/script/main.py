#!/bin/python3

from numpy import cos,sin,pi
import numpy as np
import matplotlib.pyplot as plt
from vpython import *
import PIL
import sys
sys.path.append('../../../../MetodosNumericos')
import metodos.rungekutta.rk4 as rk
sys.path.append('.')

def f(w1,w2,o1,o2,t):
    s1=sin(o1)
    s2=sin(o2)
    s=sin(o1-o2)
    c=cos(o1-o2)
    e1=msl*s*w2**2+mu*g*S1*s1
    e2=-msl*s*w1**2+m2*g*l2*s2
    return (i1*i2*msl*c*e2-i1*e1)/(1-i1*i2*msl2*c**2)

def u(w1,w2,o1,o2,t):
    s2=sin(o2)
    s=sin(o1-o2)
    c=cos(o1-o2)
    return -i2*(msl*f(w1,w2,o1,o2,t)*c-msl*s*w1**2+m2*l2*g*s2)

def V(o1,o2):
    c1=cos(o1)
    c2=cos(o2)
    return -mu*g*S1*c1-m2*g*l2*c2

def T(o1,o2,w1,w2):
    c=cos(o1-o2)
    return 0.5*((I1+ms)*w1**2+(I2+ml)*w2**2)+msl*w1*w2*c

m1=5
m2=5
M=m1+2*m2
S1=5
S2=5
l1=S1/2
l2=S2/2
r1=0.1
r2=0.1

#cilindro
I1=(1/4)*m1*r1**2+(1/3)*m1*S1**2
I2=(1/4)*m2*r2**2+(1/3)*m2*S2**2

#terminos de facilitación de calculo
mu=0.5*m1+m2
ms=m2*S1**2
ml=m2*l2**2
msl=m2*S1*l2
msl2=msl**2
i1=(I1+ms)**(-1)
i2=(I2+ml)**(-1)

g=9.81

h=0.1
n=600
run=False
def main():
    w1=np.array([0])
    w2=np.array([0])
    o1=np.array([0.3*pi])
    o2=np.array([0.4*pi])
    v=np.array([V(o1[0],o2[0])])
    k=np.array([T(o1[0],o2[0],w1[0],w2[0])])
    e=np.array([k[0]+v[0]])
    t=np.array([0])
    
    for i in range(n):
        aux=rk.order2sys2(f,u,w1[i],w2[i],o1[i],o2[i],t,h)
        w1=np.append(w1,aux[0])
        w2=np.append(w2,aux[1])
        o1=np.append(o1,aux[2])
        o2=np.append(o2,aux[3])
        v=np.append(v,V(o1[i+1],o2[i+1]))
        k=np.append(k,T(o1[i+1],o2[i+1],w1[i+1],w2[i+1]))
        e=np.append(e,k[i+1]+v[i+1])
        t=np.append(t,t[i]+h)
        print(aux)

    plt.plot(t,o1,color="blue",label="Angulo1")
    plt.plot(t,o2,color="red",label="Angulo2")
    plt.title("Angulos - tiempo")
    plt.xlabel("tiempo")
    plt.ylabel("Angulo")
    plt.grid()
    plt.legend()
    plt.show()
    plt.plot(t,k,color="red",label="Engergía Cinética")
    plt.plot(t,v,color="blue",label="Engergía Potencial")
    plt.plot(t,e,color="brown",label="Engergía Mecánica")
    plt.title("Energía - tiempo")
    plt.xlabel("tiempo")
    plt.ylabel("Energía")
    plt.legend()
    plt.show()

    plt.plot(o1,o2)
    plt.xlabel("Angulo2")
    plt.ylabel("Angulo1")
    plt.show()


    #"""
    #Vpython-Simulación

    scene=canvas(title='Péndulo doble',width=1000, height=600,center=vector(0,(l1+l2)/2,0))
    cam=Camera(scene)
    def runbutton(b):
        global run
        run=not run
        if not run: b.text='Run'
        else: b.text='Pause'

    b=button(text='Run',bind=runbutton)
    
    pivot=vector(0,S1+S2,0)
    s=sphere(pos=vector(0,S1+S2,0),mass=1,radius=0.5*(S1+S2)*0.05,color=color.white)
    point1=sphere(pos=vector(S1*sin(o1[0]),S1+S2-S1*cos(o1[0]),0),mass=m1,radius=0.5*(S1+S2)*0.07,color=color.blue,make_trail=True)
    bar1=cylinder(pos=pivot,axis=point1.pos-pivot,radius=0.5*(S1+S2)*0.02,color=color.white)
    point2=sphere(pos=vector(S1*sin(o1[0])+S2*sin(o2[0]),S1+S2-S1*cos(o1[0])-S2*cos(o2[0]),0),mass=m2,radius=0.5*(S1+S2)*0.07,color=color.red,make_trail=True)
    bar2=cylinder(pos=point1.pos,axis=point2.pos-point1.pos,radius=0.5*(S1+S2)*0.02,color=color.white)
    
    for i in range(0,n):
        sleep(0.5*h)
        while(not run):()
        point1.pos=vector(S1*sin(o1[i]),S1+S2-S1*cos(o1[i]),0)
        bar1.axis=point1.pos-bar1.pos
        point2.pos=vector(S1*sin(o1[i])+S2*sin(o2[i]),S1+S2-S1*cos(o1[i])-S2*cos(o2[i]),0)
        bar2.pos=point1.pos
        bar2.axis=point2.pos-bar2.pos
        #if i%5==0: scene.capture("pendulo_doble"+str(i/5).zfill(4))
    #"""

    
if __name__=="__main__":
    main()
