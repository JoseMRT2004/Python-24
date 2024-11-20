# Manejo de subcadenas en Python

# 1. Creación de la cadena de ejemplo
cadena = 'Hola, mundo!'

# 2. Extracción de subcadenas:
#    - Usamos índices para obtener partes de la cadena. Recordemos que el índice en Python empieza en 0.

# Subcadena que contiene 'Hola' (índices 0 a 4, excluyendo el último índice)
subcadena_hola = cadena[0:4]
print(f'Subcadena de hola: {subcadena_hola}')  # Resultado: Hola

# Subcadena que contiene 'mundo' (índices 6 a 11, excluyendo el último índice)
subcadena_mundo = cadena[6:11]
print(f'Subcadena de mundo: {subcadena_mundo}')  # Resultado: mundo

# 3. Uso del método find():
# Este método busca la primera aparición de una subcadena dentro de la cadena.
# Si la encuentra, devuelve la posición inicial. Si no, devuelve -1.

# Buscamos la posición de la letra 'm'
posicion = cadena.find("m")
print(f'Posición de "m": {posicion}')  # Resultado: 6
