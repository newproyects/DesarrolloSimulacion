import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from configparser import ConfigParser

def dx(x,y,z,t):
    return a*(y-x)

def dy(x,y,z,t):
    return x*(b-z)-y

def dz(x,y,z,t):
    return x*y-c*z


idd=int(input('indice: '))
opt=input('salida (p) , (s): ')
clr=input('color: ')
url=f'config{idd}.ini'


conf=ConfigParser()

if conf.read(url)==[]:
    print(f'Archivo no encontrado: {url}')
    exit()


print(f"\nNombre: {conf.get('meta-data','name')}\n")

print("Parametros:")
print(f"a = {conf.get('physical-parameters','a')}")
print(f"b = {conf.get('physical-parameters','b')}")
print(f"c = {conf.get('physical-parameters','c')}\n")

print("Parametros Computacionales:")
print(f"dt = {conf.get('computacional-parameters','dt')}")
print(f"n = {conf.get('computacional-parameters','n')}")


a=float(conf.get('physical-parameters','a'))
b=float(conf.get('physical-parameters','b'))
c=float(conf.get('physical-parameters','c'))
dt=float(conf.get('computacional-parameters','dt'))
n=int(conf.get('computacional-parameters','n'))
x=np.array([float(conf.get('physical-parameters','x'))])
y=np.array([float(conf.get('physical-parameters','y'))])
z=np.array([float(conf.get('physical-parameters','z'))])

t=np.linspace(0,n*dt,n)

for i in range(n):
    x=np.append(x,x[i]+dx(x[i],y[i],z[i],t[i])*dt)
    y=np.append(y,y[i]+dy(x[i],y[i],z[i],t[i])*dt)
    z=np.append(z,z[i]+dz(x[i],y[i],z[i],t[i])*dt)


fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.set_xlim(np.min(x),np.max(x))
ax.set_ylim(np.min(y),np.max(y))
ax.set_zlim(np.min(z),np.max(z))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

if clr=="":
    ax.plot(x,y,z,label=f'a={a} , b={b} , c={c} , ro=({x[0]},{y[0]},{z[0]})')
else:
    ax.plot(x,y,z,label=f'a={a} , b={b} , c={c} , ro=({x[0]},{y[0]},{z[0]})',color=clr)
plt.legend()

if opt=='p':
    plt.show()
elif opt=='s':
    plt.savefig(f'output/grafica{idd}.png')

fig.clf()

fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.set_xlim(np.min(x),np.max(x))
ax.set_ylim(np.min(y),np.max(y))
ax.set_zlim(np.min(z),np.max(z))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

if clr=="":
    line,=ax.plot(x[0],y[0],z[0],label=f'a={a} , b={b} , c={c} , ro=({x[0]},{y[0]},{z[0]})')
else:
    line,=ax.plot(x[0],y[0],z[0],label=f'a={a} , b={b} , c={c} , ro=({x[0]},{y[0]},{z[0]})',color=clr)

def update(i,x,y,z):
    line.set_data(x[:i],y[:i])
    line.set_3d_properties(z[:i])

anime=animation.FuncAnimation(fig,update,n,fargs=(x,y,z),interval=1,blit=False)

plt.legend()

if opt=='p':
    plt.show()
elif opt=='s':
    anime.save(f'output/anim{idd}.mp4')

print('---------------------------------------finish---------------------------------------')

