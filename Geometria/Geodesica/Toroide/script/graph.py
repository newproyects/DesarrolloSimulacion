import matplotlib.pyplot as plt
import numpy as np
from numpy import pi,cos,sin

def xu(u1,u2,R,r):
    return (R+r*cos(u1))*cos(u2)

def yu(u1,u2,R,r):
    return (R+r*cos(u1))*sin(u2)

def zu(u1,u2,R,r):
    return r*sin(u1)

def graph(u1,u2,P1,P2,R,r):
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')

    #Graficar curva
    x=xu(u1,u2,R,r)
    y=yu(u1,u2,R,r)
    z=zu(u1,u2,R,r)
    ax.plot(x,y,z,color='orange',lw=4)

    #Graficar puntos
    x=xu(P1[0],P1[1],R,r)
    y=yu(P1[0],P1[1],R,r)
    z=zu(P1[0],P1[1],R,r)
    ax.scatter(x,y,z,color='green',lw=2,label=rf'Punto inicial ({round(x,3)},{round(y,3)},{round(z,3)})=$\vec x$({round(u1[0],3)},{round(u2[0],3)})')

    x=xu(P2[0],P2[1],R,r)
    y=yu(P2[0],P2[1],R,r)
    z=zu(P2[0],P2[1],R,r)
    ax.scatter(x,y,z,color='red',lw=2,label=rf'Punto final ({round(x,3)},{round(y,3)},{round(z,3)})=$\vec x$({round(u1[-1],3)},{round(u2[-1],3)})')

    #Graficar toro
    o1=np.linspace(0,2*pi,40)
    o2=np.linspace(0,2*pi,40)
    o2,o1=np.meshgrid(o2,o1)

    x=xu(o1,o2,R,r)
    y=yu(o1,o2,R,r)
    z=zu(o1,o2,R,r)
    ax.plot_wireframe(x,y,z,lw=0.5)

    #Limites y titulo
    ax.set_xlim(-R-1,R+1)
    ax.set_ylim(-R-1,R+1)
    ax.set_zlim(-r-1,r+1)
    plt.title('Geodésica en Toroide')
    plt.legend()
    plt.show()
