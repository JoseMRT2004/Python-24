print('\n*** Sistema de Reserva de Hotel ***\n')

tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_con_vista_mar = 190.50

nombre_cliente = input('Nombre del Cliente: ')
dias_estadia = int(input('Días de estadía: '))
vista_al_mar_txt = input('Con vista al mar (Si/No)? ')
vista_al_mar = vista_al_mar_txt.strip().lower() == 'si'

if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_mar

# Mostramos los detalles de la reserva
print(f'''\n--------- Detalles de la Reservación ------------
Cliente: {nombre_cliente}')
Días de estadía: {dias_estadia}')
Costo total: ${costo_total:.2f}')
Habitación con vista al mar: {'Sí' if vista_al_mar else 'No'}''')