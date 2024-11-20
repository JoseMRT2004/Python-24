PIN = "1234"                   # PIN predefinido para acceder al cajero
SALDO_INICIAL = 1000           
saldo = SALDO_INICIAL          
intentos = 3                   # Intentos permitidos para ingresar el PIN

transacciones = []

while intentos > 0:  
    pin_ingresado = input("Ingrese su PIN: ")
    if pin_ingresado == PIN:
        print("¡PIN correcto! Bienvenido.")
        break                 
    else:
        intentos -= 1
        print(f"PIN incorrecto. Le quedan {intentos} intentos.")

if intentos > 0:  # Si el PIN fue correcto, se muestra el menú
    while True:
        print("\n--- Menú Cajero Automático ---")
        print("[1] - Saldo Disponible")
        print("[2] - Depositar dinero")
        print("[3] - Retirar dinero")
        print("[4] - Historial de transacciones")
        print("[5] - Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            print(f"Su saldo actual es: ${saldo}")

        elif opcion == "2":
            deposito = float(input("Ingrese la cantidad a depositar: "))
            if deposito > 0:
                saldo += deposito                 
                
                transacciones += [f"Depósito: ${deposito}"]  # Guardar la transacción en el array
                print(f"Depósito exitoso. Su nuevo saldo es: ${saldo}")
            else:
                print("La cantidad ingresada no es válida.")

        elif opcion == "3":
            retiro = float(input("Ingrese la cantidad a retirar: "))
            if 0 < retiro <= saldo:
                saldo -= retiro                   
                transacciones += [f"Retiro: ${retiro}"]  
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")
            else:
                print("No tiene suficiente saldo o la cantidad no es válida.")

        elif opcion == "4":
            print("\n--- Historial de Transacciones ---\n")
            if len(transacciones) == 0:
                print("No hay transacciones registradas.")
            else:
                indice = 1  # Inicializa el índice para numerar transacciones
                for transaccion in transacciones:
                    print(f"{indice}. {transaccion}")  # Imprime cada transacción con su índice
                    indice += 1  # Incrementar el índice manualmente

        elif opcion == "5":
            print("Gracias por usar nuestro cajero. ¡Hasta luego! 💕")
            break

        else:
            print("Opción no válida. Por favor, elija entre 1 y 5.")

else:
    print("Demasiados intentos fallidos. Su cuenta ha sido bloqueada.")
