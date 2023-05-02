# Escribe un programa Python que cree un arreglo (array) de numpy de números enteros del 1 al 10 y luego multiplique cada elemento del arreglo por 2.

import numpy as np

arreglo = np.arange(1, 11)
arreglo_multiplicado = arreglo * 2
print("El arreglo original es:", arreglo)
print("El arreglo multiplicado es:", arreglo_multiplicado)
