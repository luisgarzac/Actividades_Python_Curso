# Escribe un programa Python que pida al usuario que ingrese números hasta que ingrese -1. Luego, imprime el número más grande de la lista.

numeros = []
numero = float(input("Ingresa un número (-1 para salir): "))
while numero != -1:
    numeros.append(numero)
    numero = float(input("Ingresa otro número (-1 para salir): "))
numero_mas_grande = max(numeros)
print("El número más grande es:", numero_mas
