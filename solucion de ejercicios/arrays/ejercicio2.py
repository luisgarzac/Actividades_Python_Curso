# Escribe un programa Python que pida al usuario que ingrese 5 números y luego imprima el promedio de los números.

numeros = []
for i in range(5):
    numero = float(input("Ingresa un número: "))
    numeros.append(numero)
promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)
