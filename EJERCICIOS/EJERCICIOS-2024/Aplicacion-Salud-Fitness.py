print('\n*** Aplicación de Salud y Fitness ***')

# Constantes
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado, son kilocalorias

nombre_usuario = input('\nCuál es tu nombre? ')
pasos_diarios = int(input('\nCuántos pasos has caminado hoy? '))

meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO
meta_alcanzada_txt = 'Sí' if meta_alcanzada else 'No'
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la información

print(f'''\nUsuario: {nombre_usuario}
Pasos dados hoy: {pasos_diarios}
Calorías quemadas: {calorias_quemadas} kcal
Meta de pasos diario alcanzada: {meta_alcanzada_txt}
La meta de pasos diarios es de: {META_PASOS_DIARIO} pasos''')