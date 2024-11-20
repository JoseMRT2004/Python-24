print('*** Sistema Tienda en Línea con Descuentos ***')

MONTO_COMPRA_DESC = 1000

monto_compra = float(input('Cual fue el monto de tu compra? '))
es_miembro = input('Eres miembro de la tienda (Si/No)? ')

descuento = 0
if monto_compra >= MONTO_COMPRA_DESC and es_miembro.strip().lower() == 'si':
    descuento = 0.1  
elif es_miembro.strip().lower() == 'si':
    descuento = .05  
elif monto_compra >= MONTO_COMPRA_DESC:
    descuento = .03  
    descuento = 0

if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'''\nFelicidades, has obtenido un descuento del {descuento * 100:.0f}%
    Monto de la compra: ${monto_compra:.2f}
    Monto del descuento: ${monto_descuento:.2f}
    Monto final de la compra con descuento: ${monto_final:.2f}''')
else:
    print(f'''\nNo obtuviste ningún tipo de descuento
    Te invitamos a hacerte miembro de la tienda
    Monto final de la compra: ${monto_compra:.2f}''')