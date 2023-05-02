# Escribe un programa Python que resuelva el sistema de ecuaciones lineales 2x + y = 5 y x + y = 3 utilizando la función solve de la librería scipy.

from scipy.linalg import solve

A = [[2, 1], [1, 1]]
b = [5, 3]
solucion = solve(A, b)
print("La solución del sistema de ecuaciones es:", solucion)
