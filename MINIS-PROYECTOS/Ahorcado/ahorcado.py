'''' 
12. Juego del Ahorcado

Descripción:

Desarrolla el clásico juego del ahorcado, donde la computadora elige una 'palabra' aleatoria y el jugador debe adivinarla letra por letra.
El jugador tiene un número limitado de intento antes de perder.
Muestra al jugador las letras adivinadas correctamente y las que aún faltan '''


import random
import os
from key_word import PALABRAS
from banner import titulo, ganador, dibujo_ahorcado

seleccion = random.choice(PALABRAS)
pista = seleccion['pista']
palabra = seleccion['palabra']
progreso = ['_'] * len(palabra)
intento = 5
letras_adivinada = []

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresiona Enter para continuar...")

def mostrar_estado():
    """Muestra el estado actual del juego."""
    print(f'''
    - Tu palabra tiene {len(palabra)} letras
    - Tus letras intentadas son: {', '.join(letras_adivinada) if letras_adivinada else 'Ninguna'}
    - Progreso: {' '.join(progreso)}
    - Intentos restantes: {intento}
    ''')

def comodin():
    global intento
    if intento == 1:
        if input("\n¿Quieres una pista? (SI/NO): ").lower() == "si":
            print(f'\nPista: {pista}')
            pausar()

def jugar():
    '''Logica principal del juego'''
    global intento
    cls()

    while intento > 0:
        mostrar_estado()
        letra = input("\nAdivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("\nPor favor, ingresa solo una letra.")
            pausar()
            cls()
            continue
        if letra in letras_adivinada:
            print("\nYa intentaste esa letra. Intenta con otra.")
            pausar()
            cls()
            continue

        letras_adivinada.append(letra)

        if letra in palabra:
            for i, char in enumerate(palabra):
                if char == letra:
                    progreso[i] = letra
        else:
            intento -= 1
            print(dibujo_ahorcado(intento))
        
        comodin()
        pausar()
        cls()

        if "_" not in progreso:
            print(f'''
{ganador}
¡Felicitaciones! Adivinaste la palabra: {palabra.upper()}
            ''')
            pausar()
            break

    if intento == 0:
        print(f'''
¡Lo siento, te has quedado sin intentos!
La palabra era: {palabra.upper()}
        ''')
        pausar()

def menu():
    while True:
        cls()
        print(titulo)
        print('''
--- Menú Ahorcado ---

[1] - Jugar
[2] - Salir
        ''')
        opcion = input("Selecciona una opción: ")

        match opcion:
            case '1':
                global palabra, progreso, intento, letras_adivinada
                seleccion = random.choice(PALABRAS)
                pista = seleccion['pista']
                palabra = seleccion['palabra']
                progreso = ['_'] * len(palabra)
                intento = 5
                letras_adivinada = []
                jugar()
            case '2':
                print("\n¡Gracias por jugar! Hasta pronto.")
                pausar()
                break
            case _:
                print("\nOpción inválida. Intenta nuevamente.")
                pausar()

menu()
