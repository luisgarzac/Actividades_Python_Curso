# Escribe un programa Python que pida al usuario una cadena de texto e imprima cada palabra de la cadena en una línea separada.

cadena = input("Ingresa una cadena de texto: ")
palabras = cadena.split()
for palabra in palabras:
    print(palabra)
