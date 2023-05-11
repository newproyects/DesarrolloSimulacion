#!/bin/python3

import numpy as np
from numpy import pi,sin
import matplotlib.pyplot as plt
from vpython import *

g=9.81
l=2
m=1

h=0.01
n=10000
run=False
def main():
    t=np.array([0.0])
    o=np.array([0.999*pi])
    w=np.array([0.0])
    v=np.array([-m*g*l*cos(o[0])])
    k=np.array([0.5*m*(l*w[0])**2])
    e=np.array([k[0]+v[0]])

    for i in range(0,n):
        t=np.append(t,t[i]+h)
        w=np.append(w,w[i]-h*g*sin(o[i])/l)
        o=np.append(o,o[i]+h*w[i+1])
        v=np.append(v,m*g*(l-l*cos(o[i])))
        k=np.append(k,0.5*m*(l*w[i])**2)
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

    #"""
    #Vpython-Simulación

    scene=canvas(title='Péndulo simple',width=1000, height=600,center=vector(0,l/2,0))
    cam=Camera(scene)
    def runbutton(b):
        global run
        run=not run
        if not run: b.text='Run'
        else: b.text='Pause'

    b=button(text='Run',bind=runbutton)

    pivot=vector(0,l,0)
    s=sphere(pos=vector(0,l,0),mass=1,radius=l*0.05,color=color.white)
    point=sphere(pos=vector(0,0,0),mass=1,radius=l*0.07,color=color.red)
    bar=cylinder(pos=pivot,axis=point.pos-pivot,radius=l*0.02,color=color.white)

    for i in range(0,10000):
        sleep(2e-5)
        while(not run):()
        point.pos=vector(l*sin(o[i]),l-l*cos(o[i]),0)
        bar.axis=point.pos-bar.pos

#"""

if __name__=="__main__":
    main()
