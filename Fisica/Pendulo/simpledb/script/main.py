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
    return ((g/l1)*((m2/M)*c*s2-s1)-(m2/M)*s*(c*w1**2+L*w2**2))/(1-(m2/M)*c**2)

def u(w1,w2,o1,o2,t):
    s2=sin(o2)
    s=sin(o1-o2)
    c=cos(o1-o2)
    return -Ln*c*f(w1,w2,o1,o2,t)+Ln*s*w1**2-g*s2/l2

def V(o1,o2):
    c1=cos(o1)
    c2=cos(o2)
    return -g*M*l1*c1-g*m2*l2*c2

def T(o1,o2,w1,w2):
    c=cos(o1-o2)
    return 0.5*(M*(l1*w1)**2+m2*(l2*w2)**2)+m2*l1*l2*w1*w2*c

m1=2
m2=2
M=m1+m2
l1=1
l2=1
L=l2/l1
Ln=l1/l2
g=9.81

h=0.1
n=500
run=False
def main():
    w1=np.array([0])
    w2=np.array([0])
    o1=np.array([0.2*pi])
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

    #fle.close()
        
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
    
    pivot=vector(0,l1+l2,0)
    s=sphere(pos=vector(0,l1+l2,0),mass=1,radius=0.5*(l1+l2)*0.05,color=color.white)
    point1=sphere(pos=vector(l1*sin(o1[0]),l1+l2-l1*cos(o1[0]),0),mass=m1,radius=0.5*(l1+l2)*0.07,color=color.blue,make_trail=True)
    bar1=cylinder(pos=pivot,axis=point1.pos-pivot,radius=0.5*(l1+l2)*0.02,color=color.white)
    point2=sphere(pos=vector(l1*sin(o1[0])+l2*sin(o2[0]),l1+l2-l1*cos(o1[0])-l2*cos(o2[0]),0),mass=m2,radius=0.5*(l1+l2)*0.07,color=color.red,make_trail=True)
    bar2=cylinder(pos=point1.pos,axis=point2.pos-point1.pos,radius=0.5*(l1+l2)*0.02,color=color.white)
    
    for i in range(0,n):
        sleep(0.5*h)
        while(not run):()
        point1.pos=vector(l1*sin(o1[i]),l1+l2-l1*cos(o1[i]),0)
        bar1.axis=point1.pos-bar1.pos
        point2.pos=vector(l1*sin(o1[i])+l2*sin(o2[i]),l1+l2-l1*cos(o1[i])-l2*cos(o2[i]),0)
        bar2.pos=point1.pos
        bar2.axis=point2.pos-bar2.pos
        #if i%5==0: scene.capture("pendulo_doble"+str(int(i/5)).zfill(4))
        #if i%2==0: scene.capture("pendulo_doble"+str(int(i/2)).zfill(4))
        #scene.capture("pendulo_doble"+str(i).zfill(4))
        
    #"""

if __name__=="__main__":
    main()
