frutas = ['mango', 'manzana', 'guayaba', 'banana', 'uvas', 'peras', 'limon', 'zapote', 'mandarina', 'naranja']

while True:
    print("\n\t\t--- Menu de frutas ---\n")
    print("[1] - Listar frutas disponibles")
    print("[2] - Eliminar Fruta")
    print("[3] - Agregar Fruta")
    print("[4] - Elegir fruta Favorita")
    print("[5] - Ver número de Frutas en el inventario")
    print("[6] - Salir")

    opcion = input("\nSeleccione una opción (1-6): ")

    if opcion == "1":
        for posicion in range(0, len(frutas)):
            print(posicion, frutas[posicion])
    elif opcion == "2":
        frutaeliminada = int(input("Introduce el número de la fruta a eliminar: "))
        if 0 <= frutaeliminada < len(frutas):
            print(f"Eliminaste esta fruta: {frutas.pop(frutaeliminada)}")
        else:
            print("Número inválido. Por favor, selecciona un número válido.")
    elif opcion == "3":
        frutaagregar = input("Escribe el nombre de la fruta: ")
        frutas += [frutaagregar]
        print("Fruta agregada. La lista actualizada de frutas es:")
        for posicion in range(0, len(frutas)):
            print(posicion, frutas[posicion])
    elif opcion == "4":
        frutaelegida = int(input("Introduce el número de tu fruta elegida: "))
        if 0 <= frutaelegida < len(frutas):
            print(f"Felicidades, tu fruta elegida es: {frutas[frutaelegida]}")
        else:
            print("Número inválido. Por favor, selecciona un número válido.")
    elif opcion == "5":
        print(f"Tienes una {len(frutas)} frutas en el almacen.")
    elif opcion == "6":
        print("Gracias por usar nuestro cajero. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")
