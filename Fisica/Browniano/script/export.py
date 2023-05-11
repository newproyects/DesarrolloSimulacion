import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def export1D(data,m,h,outf):
    t=np.linspace(0,m*h,m)

    df=pd.DataFrame(columns=['ID','t','r','v'])

    for i in range(len(data)):
        df=pd.concat([df,pd.DataFrame({'ID':np.full(m,i),'t':t,'r':np.concatenate(data[i].r),'v':np.concatenate(data[i].v)})])

    t=np.linspace(0,m*h,m)
    for i in range(len(data)):
        plt.plot(t,data[i].r)

    plt.xlabel('t')
    plt.ylabel('r(t)')
    plt.show()

    for i in range(len(data)):
        plt.plot(t,data[i].v)

    plt.xlabel('t')
    plt.ylabel('v(t)')
    plt.show()

    df.to_csv(outf)

    print(f'Datos exportados al archivo >> {outf}')


def export2D(data,m,h,outf):
    t=np.linspace(0,m*h,m)

    df=pd.DataFrame(columns=['ID','t','x','y','vx','vy'])

    for i in range(len(data)):
        df=pd.concat([df,pd.DataFrame({'ID':np.full(m,i),'t':t,'x':data[i].r[:,0],'y':data[i].r[:,1],
                                       'vx':data[i].v[:,0],'vy':data[i].v[:,1]})])


    t=np.linspace(0,m*h,m)
    for i in range(len(data)):
        plt.plot(data[i].r[:,0],data[i].r[:,1])

    plt.xlabel('t')
    plt.ylabel('r(t)')
    plt.show()

    for i in range(len(data)):
        plt.plot(data[i].v[:,0],data[i].v[:,1])

    plt.xlabel('t')
    plt.ylabel('v(t)')
    plt.show()

    df.to_csv(outf)

    print(f'Datos exportados al archivo >> {outf}')


def export3D(data,m,h,outf):
    t=np.linspace(0,m*h,m)

    df=pd.DataFrame(columns=['ID','t','x','y','z','vx','vy','vz'])

    for i in range(len(data)):
        df=pd.concat([df,pd.DataFrame({'ID':np.full(m,i),'t':t,'x':data[i].r[:,0],'y':data[i].r[:,1],'z':data[i].r[:,2],
                                       'vx':data[i].v[:,0],'vy':data[i].v[:,1],'vz':data[i].v[:,2]})])


    t=np.linspace(0,m*h,m)

    ax=plt.axes(projection='3d')
    for i in range(len(data)):
        ax.plot(data[i].r[:,0],data[i].r[:,1],data[i].r[:,2])

    plt.show()

    ax=plt.axes(projection='3d')
    for i in range(len(data)):
        ax.plot(data[i].v[:,0],data[i].v[:,1],data[i].v[:,2])

    plt.show()

    df.to_csv(outf)

    print(f'Datos exportados al archivo >> {outf}')
