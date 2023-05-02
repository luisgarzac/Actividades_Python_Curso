# Escribe un programa Python que pida al usuario que ingrese números hasta que ingrese -1. Luego, imprime los números ingresados en orden inverso.

numeros = []
numero = float(input("Ingresa un número (-1 para salir): "))
while numero != -1:
    numeros.append(numero)
    numero = float(input("Ingresa otro número (-1 para salir): "))
numeros.reverse()
print(numeros)
