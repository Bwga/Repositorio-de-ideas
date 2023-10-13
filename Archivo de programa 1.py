import random

Caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

Longitud = int(input("Introduzca la longitud de su contraseña:"))

Contrasena = ""

for i in range(Longitud):
    x = random.choice(Caracteres)

    Contrasena = Contrasena + x

print(Contrasena)