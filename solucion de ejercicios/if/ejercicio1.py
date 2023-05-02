# En un programa Python, pide al usuario que ingrese un número. Si el número es positivo, imprime "El número es positivo". Si es negativo, 
# imprime "El número es negativo". Si es cero, imprime "El número es cero".

num = float(input("Ingresa un número: "))
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")
