# Escribe un programa Python que pida al usuario que ingrese 5 números y luego imprima el número más grande de los números.

numeros = []
for i in range(5):
    numero = float(input("Ingresa un número: "))
    numeros.append(numero)
numero_mas_grande = max(numeros)
print("El número más grande es:", numero_mas_grande)
