# Escribe un programa Python que cree dos arreglos (arrays) de numpy de números aleatorios entre 0 y 1 y luego calcule su producto punto (dot product).

import numpy as np

arreglo_1 = np.random.rand(3)
arreglo_2 = np.random.rand(3)
producto_punto = np.dot(arreglo_1, arreglo_2)
print("El primer arreglo es:", arreglo_1)
print("El segundo arreglo es:", arreglo_2)
print("El producto punto es:", producto_punto)
