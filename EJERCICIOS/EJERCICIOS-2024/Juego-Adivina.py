# Crea un bloque de codogo que le oida al ussuario a divinar un numero y cuneta los intentos.

import random

intentos = 0
numero_secreto = random.choice(range(1, 51))

intento_user = None

while intento_user != numero_secreto:
    intento_user = int(input('\nIntroduce el número oculto entre 1-50: '))
    if 1 <= intento_user <= 50:
        intentos += 1
        print(f'Lo has intentado: {intentos}')
            
        if intento_user == numero_secreto:
                print(f'''¡Felicidades! La posibilidad de adivinar el número es 0.02%.
                Adivinaste el número, ¡es: {numero_secreto}!''')
        else:
            print('Por favor, ingresa un valor válido entre 1 y 50.')
