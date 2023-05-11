import numpy as np
import matplotlib.pyplot as plt

def act(s):
    return 0 if s < 0 else 1

a=0.2

w=np.random.randn(3)

y=np.array([0,0,0,1])

x=np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])

ee=np.array([])
se=1

j=0
while se>0:
    se=0
    print(f"iteración: {j}")
    print(f"pesos de entrada: {w}")
    for i in range(4):
        yk=act(np.dot(w,x[i]))
        e=y[i]-yk
        se+=abs(e)
        w=w+a*e*x[i]

    ee=np.append(ee,[se])
    print(f"error acumulado: {se}")
    print(f"pesos de salida: {w}\n")
    j+=1

print(f"pesos obtenidos: {w}")

print("prueba:")

print(" x0 x1 x2 |  y")
print("---------------")

for i in range(4):
    print(f" {x[i]}  |  {act(np.dot(w,x[i]))}")


plt.plot(np.arange(j),ee,".-")
plt.xlabel("iteraciones")
plt.ylabel("error")
plt.show()
