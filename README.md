# Electro1

El programa fue realizado como un archivo de python .py, el cual se debe correr en una terminal de python mediante Visual Studio Code, Spyder u otro intérprete de python. 

El usuario debe correr el archivo el cual le preguntara algunos parametros necesarios para la simulacion en el siguiente orden:

1. Número de puntos de la red en el eje x (N)
2. Número de puntos de la red en el eje y (M)
3. Número de puntos de la red en el eje x (dx)
4. Valor correspondiente a la condición de frontera en x = 0 (extremo izquierdo) Debe ser una constante
5. Valor correspondiente a la condición de frontera en x = N*dx (extremo derecho) Debe ser una constante
6. Valor correspondiente a la condicion de frontera en y = 0 (extremo inferior)
7. Valor correspondiente a la condición de frontera en y = N*dy (extremo superior)

A partir de estos valores el programa procederá a calcular los puntos en la red mediante el promedio de sus vecinos, según lo enunciado por el metodo de relajacion. El programa grafica la solución numérica, la solución analitica y el error entre ambas.
