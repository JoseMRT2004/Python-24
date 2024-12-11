'''' 
12. Juego del Ahorcado

Descripción:

Desarrolla el clásico juego del ahorcado, donde la computadora elige una 'palabra' aleatoria y el jugador debe adivinarla letra por letra.
El jugador tiene un número limitado de intento antes de perder.
Muestra al jugador las letras adivinadas correctamente y las que aún faltan '''


import random
import os
from key_word import PALABRAS
from banner import titulo,ganador,dibujo_ahorcado

def cls():
 os.system('cls' if os.name == 'nt' else 'clear')


def jugar():
    seleccion = random.choice(PALABRAS)
    pista = seleccion['pista']
    palabra = seleccion['palabra']
    progreso = ['_'] * len(palabra)
    intento = len(palabra) + 2
    letras_adivinada = []

    while intento > 0:
        if intento == 1:
            comodin = input("\n¿Quieres una pista? (SI/NO): ").lower()
            if comodin == "si":
                print(f"\nPista: {pista}")
        print(f'\nTu palabra tiene {len(palabra)} letras.')
        print(f"\n{' '.join(progreso)}")
        letra = input("\nAdivina una letra: ").lower()

        if len(letra) != 1 or letra in letras_adivinada:
            print("Letra inválida o ya intentada. Intenta otra vez.")
            continue

        letras_adivinada.append(letra)

        if letra in palabra:
            print(f"¡Correcto! La letra '{letra}' está en la palabra.")
            for i, char in enumerate(palabra):
                if char == letra:
                    progreso[i] = letra
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            intento -= 1

        print(f'''{(dibujo_ahorcado(intento))}\nIntento disponibles: {intento}''')

        if "_" not in progreso:
            print(f"{ganador}\n¡Felicidades! La palabra era: {palabra}")
            break


def agregar_palabra():
    palabra = input("Introduce la nueva palabra: ").lower()
    pista = input("Introduce la pista para la palabra: ").lower()
    PALABRAS.append({'palabra': palabra, 'pista': pista})
    print(f"Palabra '{palabra}' agregada con éxito.")
    cls()    


def menu():
    while True:
        cls()
        print(titulo)
        print('''\n--- Menú Ahorcado ---\n
[1] - Jugar
[2] - Agregar palabra
[3] - Salir
''')
        opcion = input("Selecciona una opción: ")
        cls() 

        match opcion:
            case '1':
                jugar()
            case '2':
                agregar_palabra()
            case '3':
                print("\n¡Gracias por jugar! Hasta pronto.")
                break
            case _:
                print("\nOpción inválida. Intenta nuevamente.")

menu()
