def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def potencia(a, b):
    return a ** b

while True:
    print("\nOpciones:")  # Lista de Opciones, Interfaz
    print("[1] - Suma")
    print("[2] - Resta")
    print("[3] - Multiplicación")
    print("[4] - División")
    print("[5] - Potencia")
    print("[6] - Salir")

    opcion = int(input("\nSeleccione una opción (1-6): "))

    
    if opcion in [1, 2, 3, 4, 5]: # Si la opción no es 6, se solicitan los números
        a = float(input("Ingrese el número [A]: "))
        b = float(input("Ingrese el número [B]: "))

    
    match opcion: # Estructura match para decidir la operación
        case 1:
            print(f"Resultado de la suma: {suma(a, b):.2f}")
        case 2:
            print(f"Resultado de la resta: {resta(a, b):.2f}")
        case 3:
            print(f"Resultado de la multiplicación: {multiplicacion(a, b):.2f}")
        case 4:
            if b != 0:  # Verificación por división por cero
                print(f"Resultado de la división: {division(a, b):.2f}")
            else:
                print("Error: División por cero")
        case 5:
            print(f"Resultado de la potencia: {potencia(a, b):.2f}")
        case 6:
             print("\nGracias por usar la calculadora. ¡Hasta luego!")
             break  
        case _:
            print("\nOpción no válida")

 #======================================= COMENTA LA QUE NO QUIERAS PROBAR  =====================================================#
    
while True:
    print("\nOpciones:")  # Lista de Opciones, Interfas
    print("[1] - Suma")
    print("[2] - Resta")
    print("[3] - Multiplicación")
    print("[4] - División")
    print("[5] - Potencia")
    print("[6] - Salir")
                                        
    opcion = input("\nSeleccione una opción (1-6): ")  # Selección de opción

    if opcion in ["1", "2", "3", "4", "5"]:
        a = int(input("Ingrese el número (A): "))
        b = int(input("Ingrese el número (B): "))

        if opcion == "1":
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            print("Resultado:", division(a, b))
        elif opcion == "5":
            print("Resultado:", potencia(a, b))
    elif opcion == "6":
        print("\nGracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 6.")