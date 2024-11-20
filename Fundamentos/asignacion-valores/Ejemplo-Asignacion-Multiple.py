print('*** Operadores de Asignación ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

# Asignacion multiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

# Asignacion encadenada.
a = b = c = 10
print(f'Valor a = {a}, b = {b}, c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
# Aplicando el concepto de asignacion multiple, intercambiamos valores
x, y = y, x
print(f'Invertir los valores x = {x}, y = {y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separados por coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')