# Un programa que muestre el años segun el numero indicado:

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

mes_elegido = int(input("Introduce un número de mes (1-12): "))

if 1 <= mes_elegido <= 12:
    print(f"El mes elegido es: {meses[mes_elegido - 1]}")
else:
    print("Mes no encontrado.")
