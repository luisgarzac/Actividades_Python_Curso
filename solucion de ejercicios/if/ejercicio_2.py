# Escribe un programa Python que pida al usuario una contraseña. Si la contraseña es "contraseña123", imprime "¡Bienvenido!". 
# Si la contraseña es incorrecta, imprime "Contraseña incorrecta, vuelve a intentarlo".

password = input("Ingresa la contraseña: ")
if password == "contraseña123":
    print("¡Bienvenido!")
else:
    print("Contraseña incorrecta, vuelve a intentarlo")
