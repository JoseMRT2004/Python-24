print('*** Suma Acumulativa ***')

# Sumar los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0

# Empezamos a iterar
while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')

    acumulador_suma += numero
    numero += 1

    # Imprimir el resultado de la suma parcial
    print(f'Suma parcial acumulada: {acumulador_suma}\n')

print(f'\nResultado suma acumulada: {acumulador_suma}')