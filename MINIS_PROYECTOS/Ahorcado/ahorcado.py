import random
import os 
from key_word import PALABRAS

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def elegir_palabra():
    return random.choice(PALABRAS)

def jugar():  
    palabra_data = elegir_palabra()
    palabra = palabra_data['palabra']
    pista = palabra_data['pista']

    # Inicializar la palabra oculta
    palabra_oculta = ['_' if char.isalpha() else char for char in palabra]

    intentos = 5

    while intentos > 0:
        # Mostrar estado actual del juego
        print("\nPalabra:", " ".join(palabra_oculta))
        if intentos == 1: print("Pista:", pista)
        print("Intentos restantes:", intentos)
        cls()

        letra = input("Ingresa una letra: ").strip().lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue

        # Verificar si la letra está en la palabra
        if letra in palabra:
            for i, char in enumerate(palabra):
                if char == letra:
                    palabra_oculta[i] = char
        else:
            intentos -= 1

        if '_' not in palabra_oculta:
            print("\n¡Felicidades, has ganado! La palabra era:", palabra)
            break
    else:
        print("\n¡Perdiste! La palabra era:", palabra)

# Menú principal del juego
def menu():
    while True:
        print(f'''
=== Juego del Ahorcado ===
 
   1. Jugar
   2. Salir
             ''')

        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            jugar()
        elif opcion == '2':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida. Por favor selecciona 1 o 2.")

if __name__ == '__main__':
    menu()
