# numero_filas = int(input('Proporciona el número de filas: '))

# # Iterar sobre cada fila del triángulo
# for fila in range(1, numero_filas + 1):
#     espacios_blanco = ' ' * (numero_filas - fila)
#     asteriscos = '*' * (2 * fila - 1)
#     print(f'{espacios_blanco}{asteriscos}')


cadena = input('Introcuce una Oracion: ')
vocales = "aeiouAEIOU"
contador = 0
    
for i in cadena:
        if i in vocales:
            contador += 1
            
print(contador)