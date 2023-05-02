# Escribe un programa Python que pida al usuario que ingrese números hasta que ingrese 0. Luego, imprime los números ingresados en orden ascendente.

numeros = []
numero = float(input("Ingresa un número (0 para salir): "))
while numero != 0:
    numeros.append(numero)
    numero = float(input("Ingresa otro número (0 para salir): "))
numeros.sort()
print(numeros)
