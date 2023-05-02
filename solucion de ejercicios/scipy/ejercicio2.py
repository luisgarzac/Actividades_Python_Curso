# Escribe un programa Python que calcule la integral de la función seno de x desde 0 hasta pi utilizando la función quad de la librería scipy.

from scipy.integrate import quad
from numpy import sin, pi

resultado, error = quad(sin, 0, pi)
print("El resultado de la integral es:", resultado)
