# Escribe un programa Python que cree dos diccionarios que contengan la 
# cantidad de dinero que tienen varias personas en su cuenta corriente y luego combine los diccionarios en uno solo.

cuentas1 = {"Juan": 500, "María": 1000, "Pedro": 750}
cuentas2 = {"Ana": 1500, "Sofía": 2000}
cuentas = {**cuentas1, **cuentas2}
print("Las cuentas corrientes son:", cuentas)
