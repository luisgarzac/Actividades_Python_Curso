# Escribe un programa Python que cree un arreglo (array) de numpy de números aleatorios entre 0 y 1 y luego calcule la media y la 
# desviación estándar de los elementos del arreglo.


import numpy as np

arreglo = np.random.rand(10)
media = np.mean(arreglo)
desviacion_estandar = np.std(arreglo)
print("El arreglo es:", arreglo)
print("La media es:", media)
print("La desviación estándar es:", desviacion_estandar)
