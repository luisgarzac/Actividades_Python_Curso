# Escribe un programa Python que pida al usuario un número y imprima la tabla de multiplicar de ese número hasta 10.

num = int(input("Ingresa un número: "))
for i in range(1, 11):
    resultado = num * i
    print(num, "x", i, "=", resultado)
