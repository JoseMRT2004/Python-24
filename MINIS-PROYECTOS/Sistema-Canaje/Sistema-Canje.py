# Sistema de puntos canjeables por objetos

# Objetivos:
#   - Crear un array para almacenar los puntos del usuario.  ✅
#   - Convertir los valores del array a enteros para realizar operaciones matemáticas. ✅
#   - Implementar una condicional para comparar los puntos del usuario con el costo de los objetos. ✅
#   - Restar los puntos utilizados al total del usuario y mostrar el nuevo saldo. ✅
#   - Permitir al usuario seleccionar un objeto y realizar el canje. ✅
#   - Agragarle un usuario que pueda modificar los objetos los descuentos y los Productos ademas modificar el valor de los puntos. ✅


# Consideraciones adicionales:
#   - **Validación de datos:** Asegurarse de que el usuario ingrese valores válidos (por ejemplo, números enteros positivos). ✅
#   - **Mensajes de error:** Informar al usuario si no tiene suficientes puntos para realizar un canje. ✅
#   - **Interfaz de usuario:** Diseñar una interfaz intuitiva para que el usuario pueda navegar fácilmente por las opciones de canje. ✅
#   - **Persistencia de datos:** Considerar cómo almacenar los puntos del usuario de forma persistente (por ejemplo, en un archivo o base de datos).
#   - **Escalabilidad:** Planificar cómo agregar nuevos objetos al catálogo sin modificar mucho el código. ✅



import os
import random 

from diccionario import preguntas_respuestas,productos_canjeables

puntos_usuario = 0
historial = []

def mostrar_productos():
    global puntos_usuario
    print("\n\t--- Productos Disponibles ---")
    for i, producto in enumerate(productos_canjeables, start=1):
        print(f"{i}. {producto['nombre']} - {producto['puntos']} puntos")

    seleccion = int(input("\nElige un producto para canjear (número): ")) - 1
    if 0 <= seleccion < len(productos_canjeables) and puntos_usuario >= productos_canjeables[seleccion]['puntos']:
        puntos_usuario -= productos_canjeables[seleccion]['puntos']
        historial.append(f"Canjeado {productos_canjeables[seleccion]['nombre']} por {productos_canjeables[seleccion]['puntos']} puntos.")
        print(f"Canje exitoso. Puntos restantes: {puntos_usuario}")
    else:
        print("Puntos insuficientes o opción no válida.")
    input("\nPresiona Enter para volver al menú...")

def ver_historial():
    print("\n\t--- Historial de Canjes ---")
    if historial:
        for transaccion in historial:
            print(transaccion)
    else:
        print("No hay canjes registrados.")
    input("\nPresiona Enter para volver al menú...")

def responder_pregunta():
    global puntos_usuario
    pregunta = preguntas_respuestas[random.randint(1, 9)]
    respuesta_usuario = input(f"\nPregunta: {pregunta['pregunta']} ").lower()
    if respuesta_usuario == pregunta['respuesta']:
        puntos_usuario += pregunta['puntos']
        print(f"¡Correcto! Ganaste {pregunta['puntos']} puntos.")
    else:
        print("Respuesta incorrecta.")
    input("\nPresiona Enter para continuar...")

def menu():
    global puntos_usuario
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\nPuntos actuales: {puntos_usuario}\n')
        print('1. Canjear producto\n2. Ver historial\n3. Responder pregunta\n4. Salir')
        opcion = input("\nSelecciona una opción: ")
        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            ver_historial()
        elif opcion == '3':
            responder_pregunta()
        elif opcion == '4':
            break

menu()
