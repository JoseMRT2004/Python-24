''' Crear el juego clásico de Piedra, Papel o Tijeras:
 - El jugador competirá contra la CPU, que generará su elección de forma aleatoria.
 - Mostrar mensajes claros indicando las elecciones de ambos y quién ganó la ronda.

 EXTRA: Agregar un modo de juego para dos jugadores donde ambos ingresen sus elecciones.
 EXTRA: Implementar un marcador para registrar las victorias y permitir múltiples rondas.
 EXTRA: Incluir la opción de salir del juego al finalizar cualquier ronda.'''


import random

# Lista de objetos con las opciones
object = [
    {'nombre': 'PIEDRA', 'emoji': '🪨', 'valor': 3},
    {'nombre': 'PAPEL', 'emoji': '📄', 'valor': 1},
    {'nombre': 'TIJERA', 'emoji': '✂️', 'valor': 2}
]

# Función del menú
def menu():
    print(f'''\n
        ================================
            [SELECCIONA UNA OPCION]         
        ================================
              [1] - {object[0]["nombre"]} {object[0]["emoji"]}
              [2] - {object[1]["nombre"]} {object[1]["emoji"]}
              [3] - {object[2]["nombre"]} {object[2]["emoji"]}
              [4] - Salir
        ================================\n''')

def juego():
    while True:
        menu() 
        try:
            PLAYER_1 = int(input('\tSelecciona Una Opcion [1-4]: '))

            if PLAYER_1 == 4:
                print("¡Gracias por jugar!")
                break  

            if PLAYER_1 < 1 or PLAYER_1 > 3:
                print("Opción no válida. Por favor, selecciona entre 1 y 3.")
                continue

           
            CPU_PLAYER = random.choice(object)
            CPU_EMOJI = CPU_PLAYER['emoji']
            CPU_VALOR = CPU_PLAYER['valor']
            CPU_NOMBRE = CPU_PLAYER['nombre']

            
            SELECCION = object[PLAYER_1 - 1]  
            PLAYER_1_EMOJI = SELECCION['emoji']
            PLAYER_1_VALOR = SELECCION['valor']
            PLAYER_1_NOMBRE = SELECCION['nombre']

            print(f'''\n     
        Tu selección: {PLAYER_1_NOMBRE} {PLAYER_1_EMOJI}
        Selección de la CPU: {CPU_NOMBRE} {CPU_EMOJI}\n''')

            if PLAYER_1_VALOR == CPU_VALOR:
                print("¡Empate! Ambos eligieron la misma opción.")
            elif (PLAYER_1_VALOR == 1 and CPU_VALOR == 3) or (PLAYER_1_VALOR == 2 and CPU_VALOR == 1) or (PLAYER_1_VALOR == 3 and CPU_VALOR == 2):
                print("¡Felicidades, ganaste!")
            else:
                print("Lo siento, perdiste. ¡Mejor suerte la próxima vez!")
        
        except ValueError:
            print("Por favor ingresa un número válido.")
            
juego()

