import numpy as np
import matplotlib.pyplot as plt
from numpy import e

def ep(x):
    return alpha*b*(1+e**(-2*x*a))

def em(x):
    return alpha*b*(1-e**(-2*x*a))

def fp(x):
    return x-ep(x)

def fm(x):
    return x-em(x)

def dfp(x):
    return 1+2*a*alpha*b*e**(-2*x*a)

def dfm(x):
    return 1-2*a*alpha*b*e**(-2*x*a)

b=4
alpha=0.55
a=2

k=np.linspace(-0.1,4.2)

kp=np.array([0.1])
km=np.array([0.68])

err=1
erm=0.001
n=200
for i in range(n):
    kp=np.append(kp,kp[i]-fp(kp[i])/dfp(kp[i]))
    err=abs((kp[i+1]-kp[i])/kp[i+1])
    plt.plot([kp[i],kp[i+1]],[fp(kp[i]),0],color='blue')
    plt.plot([kp[i+1],kp[i+1]],[0,fp(kp[i+1])],'--',color='blue')
    if err<=erm:
        break

print("resultados:")

kp=kp[-1]
print(f"kp: {kp}")

#Newton-Raphson kp
plt.plot(k,fp(k),color='red',label=r'$k_+-\alpha\beta\left(1+ e^{-2k_+ a}\right)$')

plt.plot([kp,kp],[min(fp(k)),max(fp(k))],'--',color='orange')

plt.axhline(0,color='black')

plt.title(rf'Newton-Raphson $k_+ , a={a} , \alpha=${alpha} , $\beta=${b}')
plt.xlabel('$k$')
plt.legend()
plt.show()

for i in range(n):
    km=np.append(km,km[i]-fm(km[i])/dfm(km[i]))
    err=abs((km[i+1]-km[i])/km[i+1])
    plt.plot([km[i],km[i+1]],[fm(km[i]),0],color='purple')
    plt.plot([km[i+1],km[i+1]],[0,fm(km[i+1])],'--',color='purple')
    if err<=erm:
        break

km=km[-1]
print(f"km: {km}")

#Newton-Raphson km
plt.plot(k,fm(k),color='blue',label=r'$k_--\alpha\beta\left(1- e^{-2k_- a}\right)$')

plt.plot([km,km],[min(fm(k)),max(fm(k))],'--',color='green')

plt.axhline(0,color='black')

plt.title(rf'Newton-Raphson $k_- , a={a} , \alpha=${alpha} , $\beta=${b}')
plt.xlabel('$k$')
plt.legend()
plt.show()

#Soluciónes de k
plt.plot(k,k,color='brown',label='k')
plt.plot(k,ep(k),color='red',label=r'$\alpha\beta(1+e^{-2ka})$')
plt.plot(k,em(k),color='blue',label=r'$\alpha\beta(1-e^{-2ka})$')

plt.plot([kp,kp],[min(ep(k)),max(ep(k))],'--',color='orange',label=rf'$k=k_+=${kp}')
plt.plot([km,km],[min(em(k)),max(em(k))],'--',color='green',label=rf'$k=k_-=${km}')

plt.title('Soluciones de $k$')
plt.legend()
plt.show()


Ep=-(kp**2)/(2*b)
Em=-(km**2)/(2*b)

Ap=np.sqrt((kp*(1+e**(2*kp*a))**2)/(2*(e**(2*kp*a)+2*kp*a+1)))
Am=np.sqrt((km*(1-e**(2*km*a))**2)/(2*(e**(2*km*a)-2*km*a-1)))

Cp=Ap/(1+e**(2*kp*a))
Cm=-Am/(1-e**(2*km*a))

print(f"Ep: {Ep}")
print(f"Em: {Em}")
print(f"Ap: {Ap}")
print(f"Am: {Am}")

x1=np.linspace(-3,-a)
x2=np.linspace(-a,a)
x3=np.linspace(a,3)

plt.plot(x1,Ap*e**(kp*x1),color='red')
plt.plot(x2,Cp*(e**(-kp*x2)+e**(kp*x2)),color='red')
plt.plot(x3,Ap*e**(-kp*x3),color='red')
plt.title(f'Función par $\psi_+(x)$ , $E_+=${Ep}')
plt.ylabel('$\psi_+(x)$')
plt.xlabel('$x$')
plt.show()

plt.plot(x1,Am*e**(kp*x1),color='blue')
plt.plot(x2,Cm*(e**(-kp*x2)-e**(kp*x2)),color='blue')
plt.plot(x3,-Am*e**(-kp*x3),color='blue')
plt.title(f'Función impar $\psi_-(x)$ , $E_-=${Em}')
plt.ylabel('$\psi_-(x)$')
plt.xlabel('$x$')
plt.show()
