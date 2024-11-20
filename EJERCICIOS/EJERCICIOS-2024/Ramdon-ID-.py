import random

print("\n**** Generador de (ID) Unicos ****\n")

Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Nacido = input("Ingrese su año de nacimento (YYYY): ")

ID = random.randint(1000, 9999)

# Normalizar apellido y nombre
Nombre_Norm = Nombre.strip().upper()
Apellido_Norm = Apellido.strip().upper()

print(f"\nHola {Nombre}\n Tu (ID) unico es: {Nombre_Norm[:2]}{Apellido_Norm[:2]}{Nacido[:4]}{ID}")


