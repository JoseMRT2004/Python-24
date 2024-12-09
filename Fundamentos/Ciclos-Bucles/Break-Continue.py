print('*** break y continue ***')

# Ejemplo con break
print('Palabra break:')
for numero in range(1, 10):
    if numero % 2 == 0:  # numero par
        print(numero)
        break  # Salimos del ciclo inmediatamente

# Ejemplo con continue
print('\nPalabra continue: ')
for numero in range(1, 10):
    if numero % 2 == 1:  # numero impar
        continue
    print(numero)  # numeros pares