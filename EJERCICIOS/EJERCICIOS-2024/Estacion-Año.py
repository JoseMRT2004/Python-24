print('*** Estación del Año ***')

mes = int(input('Proporciona el valor del mes (1-12): '))
estacion = None
# Revisión del mes proporcionado
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Estación desconocida'
# Imprimir el resultado
print(f'La estación para el mes {mes} es {estacion}')
