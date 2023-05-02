# Escribe un programa Python que pida al usuario que ingrese números hasta que ingrese 0. Luego, imprime la suma de los números ingresados.

numeros = []
numero = float(input("Ingresa un número (0 para salir): "))
while numero != 0:
    numeros.append(numero)
    numero = float(input("Ingresa otro número (0 para salir): "))
suma = sum(numeros)
print("La suma de los números es:", suma)
