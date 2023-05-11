#!/bin/python3

from numpy import cos,sin,pi
import numpy as np
import matplotlib.pyplot as plt
from vpython import *
import PIL
import sys
sys.path.append('../../../MetodosNumericos')
import metodos.rungekutta.rk4 as rk
sys.path.append('.')

def f(w,q,o,r,t):
    return -2*w*q/r

def u(w,q,o,r,t):
    return 0.5*r*w**2-0.5*g

def V(r):
    return m*g*(r-L)

def T(o,r,w,q):
    return 0.5*m*(2*q**2+(r*w)**2)

m1=2
m2=2
m=m1
L=10
g=9.81

h=0.1
n=500
run=False
def main():
    w=np.array([0.5*pi])
    q=np.array([0])
    o=np.array([0])
    r=np.array([L/2])
    v=np.array([V(r[0])])
    k=np.array([T(o[0],r[0],w[0],q[0])])
    e=np.array([k[0]+v[0]])
    t=np.array([0])

    #w=np.array([sqrt(g/r[0])])
    
    for i in range(n):
        aux=rk.order2sys2(f,u,w[i],q[i],o[i],r[i],t,h)
        w=np.append(w,aux[0])
        q=np.append(q,aux[1])
        o=np.append(o,aux[2])
        r=np.append(r,aux[3])
        v=np.append(v,V(r[i+1]))
        k=np.append(k,T(o[i+1],r[i+1],w[i+1],q[i+1]))
        e=np.append(e,k[i+1]+v[i+1])
        t=np.append(t,t[i]+h)
        #print(aux)

    #fle.close()
    
    plt.plot(t,o,color="blue",label="Angulo")
    plt.title("Angulo - tiempo")
    plt.xlabel("tiempo")
    plt.ylabel("Angulo")
    plt.grid()
    plt.legend()
    plt.show()
    plt.plot(t,r,color="red",label="Radio")
    plt.title("Radio - tiempo")
    plt.xlabel("tiempo")
    plt.ylabel("Radio")
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

    #"""
    #Vpython-Simulación

    scene=canvas(title='Mesa',width=1000, height=600,center=vector(0,0,0))
    cam=Camera(scene)
    def runbutton(b):
        global run
        run=not run
        if not run: b.text='Run'
        else: b.text='Pause'

    b=button(text='Run',bind=runbutton)
    
    pivot=vector(0,0,0)
    #s=sphere(pos=vector(0,l1+l2,0),mass=1,radius=0.5*(l1+l2)*0.05,color=color.white)
    point1=sphere(pos=vector(r[0]*cos(o[0]),r[0]*sin(o[0]),0),mass=m1,radius=0.5*L*0.07,color=color.blue,make_trail=True)
    bar1=cylinder(pos=pivot,axis=point1.pos,radius=0.5*L*0.02,color=color.white)
    point2=sphere(pos=vector(0,0,r[0]-L),mass=m2,radius=0.5*L*0.07,color=color.red,make_trail=True)
    bar2=cylinder(pos=pivot,axis=point2.pos,radius=0.5*L*0.02,color=color.white)
    mesa=cylinder(pos=vector(0,0,-0.5*L*0.07),axis=vector(0,0,-0.5*L*0.07-L*0.01),radius=L,color=color.white,opacity=0.05)
    #resorte=helix(pos=pivot,axis=point2.pos,radius=0.1*L,coils=20,color=color.red,thickness=0.1)
    
    for i in range(0,n):
        sleep(0.5*h)
        while(not run):()
        point1.pos=vector(r[i]*cos(o[i]),r[i]*sin(o[i]),0)
        bar1.axis=point1.pos
        point2.pos=vector(0,0,r[i]-L)
        #bar2.pos=point1.pos
        bar2.axis=point2.pos
        #resorte.axis=point2.pos
        #if i%5==0: scene.capture("pendulo_doble"+str(int(i/5)).zfill(4))
        #if i%3==0: scene.capture("pendulo_doble"+str(int(i/3)).zfill(4))
        #if i%2==0: scene.capture("pendulo_doble"+str(int(i/2)).zfill(4))
        #scene.capture("pendulo_doble"+str(i).zfill(4))
    #"""

if __name__=="__main__":
    main()
