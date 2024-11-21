import random
import os

# Títulos y arte ASCII
titulo = '''\n============================================================================================================
     ___       __    __    ______   .______        ______      ___       _______    ______        _______.
    /   \     |  |  |  |  /  __  \  |   _  \      /      |    /   \     |       \  /  __  \      /       |
   /  ^  \    |  |__|  | |  |  |  | |  |_)  |    |  ,----'   /  ^  \    |  .--.  ||  |  |  |    |   (----`
  /  /_\  \   |   __   | |  |  |  | |      /     |  |       /  /_\  \   |  |  |  ||  |  |  |     \   \    
 /  _____  \  |  |  |  | |  `--'  | |  |\  \----.|  `----. /  _____  \  |  '--'  ||  `--'  | .----)   |   
/__/     \__\ |__|  |__|  \______/  | _| `._____| \______|/__/     \__\ |_______/  \______/  |_______/    
============================================================================================================'''

ganador = '''\n==================================================================
____    __    ____  __  .__   __. .__   __.  _______ .______         
\   \  /  \  /   / |  | |  \ |  | |  \ |  | |   ____||   _  \        
 \   \/    \/   /  |  | |   \|  | |   \|  | |  |__   |  |_)  |       
  \            /   |  | |  . `  | |  . `  | |   __|  |      /        
   \    /\    /    |  | |  |\   | |  |\   | |  |____ |  |\  \----.   
    \__/  \__/     |__| |__| \__| |__| \__| |_______|| _| `._____|   
=================================================================='''

perdedor = '''\n==============================================================================================
  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______         
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \        
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |       
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /        
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.   
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|   
==============================================================================================='''

# Lista de palabras con sus pistas
PALABRAS = [
    {'palabra': 'caballo', 'pista': 'animal veloz'},
    {'palabra': 'mariposa', 'pista': 'insecto con alas coloridas'},
    {'palabra': 'python', 'pista': 'lenguaje de programación'},
    {'palabra': 'manzana', 'pista': 'fruta roja o verde'},
    {'palabra': 'elefante', 'pista': 'animal grande con trompa'},
    {'palabra': 'avion', 'pista': 'vehículo que vuela'},
    {'palabra': 'computadora', 'pista': 'máquina que usas para programar'},
    {'palabra': 'jirafa', 'pista': 'animal de cuello largo'},
    {'palabra': 'refrigerador', 'pista': 'electrodoméstico para mantener comida fría'},
]

# Función de dibujo del ahorcado
def dibujo_ahorcado(intentos):
    # Arte ASCII según los intentos
    match intentos:
        case 6:
            return '''
             -----
             |   |
                 |
                 |
                 |
                 |
            ---------'''
        case 5:
            return '''
             -----
             |   |
             O   |
                 |
                 |
                 |
            ---------'''
        case 4:
            return '''
             -----
             |   |
             O   |
             |   |
                 |
                 |
            ---------'''
        case 3:
            return '''
             -----
             |   |
             O   |
            /|   |
                 |
                 |
            ---------'''
        case 2:
            return '''
             -----
             |   |
             O   |
            /|\\  |
                 |
                 |
            ---------'''
        case 1:
            return '''
             -----
             |   |
             O   |
            /|\\  |
            /    |
                 |
          ---------'''
        case 0:
            return f"{perdedor}\n"

# Función para jugar
def jugar():
    seleccion = random.choice(PALABRAS)
    palabra = seleccion['palabra']
    pista = seleccion['pista']
    progreso = ['_'] * len(palabra)
    intentos = len(palabra) + 2
    letras_adivinadas = []

    while intentos > 0:
        if intentos == 1:
            comodin = input("\n¿Quieres una pista? (SI/NO): ").lower()
            if comodin == "si":
                print(f"Pista: {pista}")

        print(f'\nTu palabra tiene {len(palabra)} letras.')
        print(f"\n{' '.join(progreso)}")
        letra = input("\nAdivina una letra: ").lower()

        if len(letra) != 1 or letra in letras_adivinadas:
            print("Letra inválida o ya intentada. Intenta otra vez.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print(f"¡Correcto! La letra '{letra}' está en la palabra.")
            for i, char in enumerate(palabra):
                if char == letra:
                    progreso[i] = letra
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            intentos -= 1

        print(dibujo_ahorcado(intentos))

        if "_" not in progreso:
            print(f"{ganador}\n¡Felicidades! La palabra era: {palabra}")
            return

    print(f"{perdedor}\nLa palabra era: {palabra}. ¡Intenta de nuevo!")

# Función para agregar una palabra
def agregar_palabra():
    palabra = input("Introduce la nueva palabra: ").lower()
    pista = input("Introduce la pista para la palabra: ").lower()
    PALABRAS.append({'palabra': palabra, 'pista': pista})
    print(f"Palabra '{palabra}' agregada con éxito.")

# Menú principal
def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(titulo)
        print('''\n--- Menú Ahorcado ---\n
[1] - Jugar
[2] - Agregar palabra
[3] - Salir
''')
        opcion = input("Selecciona una opción: ")

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
