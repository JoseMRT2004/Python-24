def verificar_pin(pin_ingresado):
    return pin_ingresado == PIN

def mostrar_saldo(saldo):
    return f"Su saldo actual es: ${saldo}"

def realizar_deposito(saldo, transacciones):
    deposito = float(input("Ingrese la cantidad a depositar: "))
    if deposito > 0:
        saldo += deposito
        transacciones.append(f"Depósito: ${deposito}")
        return saldo, f"Depósito exitoso. Su nuevo saldo es: ${saldo}"
    else:
        return saldo, "La cantidad ingresada no es válida."

def realizar_retiro(saldo, transacciones):
    retiro = float(input("Ingrese la cantidad a retirar: "))
    if 0 < retiro <= saldo:
        saldo -= retiro
        transacciones.append(f"Retiro: ${retiro}")
        return saldo, f"Retiro exitoso. Su nuevo saldo es: ${saldo}"
    else:
        return saldo, "No tiene suficiente saldo o la cantidad no es válida."

def mostrar_historial(transacciones):
    if len(transacciones) == 0:
        return "No hay transacciones registradas."
    else:
        historial = "\n--- Historial de Transacciones ---\n"
        for i, transaccion in enumerate(transacciones, 1):
            historial += f"{i}. {transaccion}\n"
        return historial

def mostrar_menu():
    return """
    --- Menú Cajero Automático ---
    
    [1] - Saldo Disponible
    [2] - Depositar dinero
    [3] - Retirar dinero
    [4] - Historial de transacciones
    [5] - Salir
    
    """

PIN = "1234"
SALDO_INICIAL = 1000
saldo = SALDO_INICIAL
intentos = 3
transacciones = []

while intentos > 0:
    pin_ingresado = input("Ingrese su PIN: ")
    if verificar_pin(pin_ingresado):
        print(f"*** ¡PIN correcto! Bienvenido. ***")
        break
    else:
        intentos -= 1
        print(f"*** PIN incorrecto. Le quedan {intentos} intentos. ***")

if intentos > 0:
    while True:
        print(mostrar_menu())
        opcion = input("Seleccione una opción (1-5): ")

        match opcion:
            case "1":
                print(f"*** {mostrar_saldo(saldo)} ***")
            case "2":
                saldo, mensaje = realizar_deposito(saldo, transacciones)
                print(f"*** {mensaje} ***")
            case "3":
                saldo, mensaje = realizar_retiro(saldo, transacciones)
                print(f"*** {mensaje} ***")
            case "4":
                print(f"*** {mostrar_historial(transacciones)} ***")
            case "5":
                print("*** Gracias por usar nuestro cajero. ¡Hasta luego! 💕 ***")
                break 
            case _:
                print("*** Opción no válida. Por favor, elija entre 1 y 5. ***")

else:
    print("*** Demasiados intentos fallidos. Su cuenta ha sido bloqueada. ***")