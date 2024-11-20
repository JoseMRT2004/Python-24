# Definimos una cadena original
cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}')

# Convertir la cadena a mayúsculas
mayusculas = cadena1.upper()  # Usamos el método upper() para convertir a mayúsculas
print(f'Cadena en mayúsculas: {mayusculas}')

# Convertir la cadena a minúsculas
print(f'Cadena en minúsculas: {cadena1.lower()}')  # Usamos el método lower() para convertir a minúsculas

# Definimos otra cadena con espacios
cadena2 = ' Juan Perez '
print(f'Cadena con espacios: {cadena2}')

# Eliminar espacios al inicio y al final de la cadena
print(f'Cadena sin espacios: {cadena2.strip()}')  # Usamos el método strip() para eliminar espacios

# Definimos una tercera cadena
cadena3 = 'Parangaricutirimícuaro'

# Obtener el largo de la cadena
# Nota: len() no es un método de cadena, es una función incorporada de Python que devuelve la longitud de cualquier objeto iterable
print(f'Largo de la cadena: {len(cadena3)}')  # Usamos la función len() para saber el largo de la cadena
