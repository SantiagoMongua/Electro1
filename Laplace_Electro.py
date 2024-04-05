"""
Desarrollado para el FISI 2632 - Electromagnetismo 1 de la Universidad de los Andes

Santiago Mongua 
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from tqdm import tqdm

def InitT(f1,f2,f3,f4,N,M):
    """
    Inicializa la matriz de potencial eléctrico utilizando las condiciones de frontera

    Args:
        f1 (float): Condición de frontera en x = 0 (extremo izquierdo)
        f2 (float): Condición de frontera en x = N*dx (extremo derecho)
        f3 (float): Condición de frontera en y = 0 (extremo inferior)
        f4 (float): Condición de frontera en y = M*dx (extremo superior)
        N (int): Número de puntos de la red en el eje x
        M (int): Número de puntos de la red en el eje y

    Returns:
        T (array): Matriz de potencial eléctrico con condiciones de frontera
    """
    T = np.zeros((N,M))
    T[0,:] = f1
    T[-1,:] = f2
    T[:,0] = f3
    T[:,-1] = f4
    
    return T

def analitica(A,x,y,a,b,f4):
    for i in range (1,len(A)-1):
        for j in range(1,len(A[0])-1):
            for n in range (1,102,2):
                kn = ((n * np.pi) / a)
                A[i,j] += (4 * f4 / np.pi) * (np.sin(kn*x[i])/n) * (np.cosh(kn*y[j])-(((1 + np.cosh(kn*b))/(np.sinh(kn*b)))*np.sinh(kn*y[j])))
    return A

def Relajacion(T,Nit = int(1e5), omega = 0.5 ,tolerancia = 1e-3):
    """
    Ejecuta el método de relajación para resolver la ecuación de Laplace numéricamente.

    Args:
    - T: Matriz de potencial eléctrico inicial con las condiciones iniciales de frontera. 
    - Nit: Número máximo de iteraciones.
    - omega: Parámetro de relajación.
    - tolerance: Criterio de convergencia.

    Returns:
    - T (array): Matriz de potencial eléctrico después de la relajación.
    - itmax (int): Número de iteraciones ejecutadas.
    """
    itmax = 0
    for it in tqdm(range(Nit)):
        dmax = 0.
        for i in range(1, len(T)-1):
            for j in range(1, len(T[0])-1):
                tmp = 0.25*( T[i+1,j] + T[i-1,j] + T[i,j+1] + T[i,j-1] )
                # Matriz resta
                r = omega*(tmp - T[i,j])
                T[i,j] += r
                
                if np.abs(r) > dmax:
                    dmax = r
        
        if np.abs(dmax) < tolerancia:
            
            print(it)
            itmax = it
            break
            
    return T,itmax

def ejecutar():
    """
    Ejecuta el solucionador de la ecuación de Laplace en dos dimensiones cartesianas mediante el método de relajación.
    De hecho, grafica la solución obtenida numéricamente, la solución 
    """
    N = int(input("Ingrese el número de puntos de la red en el eje x (N): "))
    M = int(input("Ingrese el número de puntos de la red en el eje y (M): "))
    dx = float(input("Ingrese la distancia entre puntos de la red en el eje x (dx): "))
    f1 = float(input("Ingrese el valor correspondiente a la condición de frontera en x = 0 (extremo izquierdo): "))
    f2 = float(input("Ingrese el valor correspondiente a la condición de frontera en x = N*dx (extremo derecho): "))
    f3 = float(input("Ingrese el valor correspondiente a la condición de frontera en y = 0 (extremo inferior): "))
    f4 = float(input("Ingrese el valor correspondiente a la condición de frontera en y = N*dy (extremo superior): "))
    
    """Ejecución de funciones correspondientes al cálculo numérico de la ecuación de Laplace"""
    dy = dx
    a = N*dx
    b = M*dy
    x = np.linspace(0,N*dx,N)
    y = np.linspace(0,M*dy,M)
    T = InitT(f1,f2,f3,f4,N,M)
    A = InitT(f1,f2,f3,f4,N,M)
    Tf1,_ = Relajacion(T)
    Af = analitica(A,x,y,a,b,f4)
    print(Af)
    """Graficación de la solución obtenida para la ecuación de Laplace"""
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(221)
    ax1 = fig.add_subplot(222, projection='3d')
    ax2 = fig.add_subplot(223)
    ax3 = fig.add_subplot(224, projection='3d')
    X,Y = np.meshgrid(x,y)

    c = ax.contourf(X,Y,Tf1.T)
    d = ax2.contourf(X,Y,Af.T)
    ax1.plot_surface(X,Y,Tf1.T)
    ax3.plot_surface(X,Y,Af.T)
    plt.show()   

ejecutar()
