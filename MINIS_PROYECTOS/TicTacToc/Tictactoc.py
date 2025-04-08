import os
from random import randrange

def crear_tablero():
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']] 

# Mostrar el tablero de forma visualmente atractiva
def mostrar_tablero(tablero):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla para mayor claridad
    print("\033[1;34m=== Tres en Línea ===\033[0m")
    print("\033[1;32mJugador: O | Ordenador: X\033[0m\n")
    
    # Imprimir las filas del tablero
    for fila in tablero:
        print(f" \033[1;37m{' | '.join(fila)}\033[0m")
        print(" ---+---+--- ")

# Convertir un número del tablero en coordenadas de fila y columna
def numero_a_coordenadas(numero):
    numero = int(numero) - 1  # Restamos 1 para usar índices basados en 0
    return numero // 3, numero % 3

def hay_victoria(tablero, simbolo):

    for i in range(3):
        if all(tablero[i][j] == simbolo for j in range(3)) or \
           all(tablero[j][i] == simbolo for j in range(3)):
            return True
    
    # Revisar las dos diagonales
    if all(tablero[i][i] == simbolo for i in range(3)) or \
       all(tablero[i][2 - i] == simbolo for i in range(3)):
        return True

    return False

# Comprobar si hay empate (cuando no hay casillas vacías)
def hay_empate(tablero):
    return all(celda in ['X', 'O'] for fila in tablero for celda in fila)

# Manejar el turno del jugador
def turno_jugador(tablero):
    while True:
        entrada = input("\033[1;33mTu turno elige un número del 1-9: \033[0m")
        if entrada.isdigit() and 1 <= int(entrada) <= 9:
            fila, col = numero_a_coordenadas(entrada)
            if tablero[fila][col] not in ['X', 'O']:  # Verificar si la casilla está libre
                tablero[fila][col] = 'O'  # El jugador pone una 'O'
                return
            else:
                print("\033[1;31mEsa casilla ya está ocupada. Intenta con otro número ⚠️ \033[0m")
        else:
            print("\033[1;31mEntrada inválida. Debes elegir un número del 1 al 9 ⚠️ \033[0m")

# Manejar el turno del ordenador (elige una casilla libre al azar)
def turno_ordenador(tablero):
    print("\033[1;36mTurno del ordenador...\033[0m")
    casillas_libres = [(f, c) for f in range(3) for c in range(3) if tablero[f][c] not in ['X', 'O']]
    if casillas_libres:
        fila, col = casillas_libres[randrange(len(casillas_libres))]
        tablero[fila][col] = 'X'  # El ordenador pone una 'X'

def jugar():
    print("\033[1;34m=== Bienvenido a Tres en Línea ===\033[0m")
    tablero = crear_tablero()  # Inicializar el tablero

    while True:
        mostrar_tablero(tablero)  # Mostrar el tablero actualizado

        if hay_victoria(tablero, 'X'):
            print("\033[1;31m💻 El ordenador ha ganado. ¡Suerte la próxima!\033[0m")
            break
        
        if hay_empate(tablero):
            print("\033[1;33m🤝 ¡Empate!\033[0m")
            break

        turno_jugador(tablero)
        mostrar_tablero(tablero)

        if hay_victoria(tablero, 'O'):
            print("\033[1;32m🎉 ¡Felicidades, ganaste!\033[0m")
            break
        
        # Verificar si hay empate después del turno del jugador
        if hay_empate(tablero):
            print("\033[1;33m🤝 ¡Empate!\033[0m")
            break

        turno_ordenador(tablero)

if __name__ == "__main__":
    jugar()  # Iniciar el juego
