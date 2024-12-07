print(f'''Crea un sistema para determinar el precio de un envio tomando en cuenta:
  (Peso en Kilogramos) y si es (Nacional o Internacional)''')
  

nombre_articulo = input('\nIntroduce el nombre del articulo que enviaras: ').lower().strip()
tipo_destino = input('Introduce el tipo de destino (Nacional o Internacional): ').lower().strip()
peso_kilogramo = float(input('Introduce el peso del articulo en Kilogramos: '))

nacional_precio = 10 * peso_kilogramo
internacional_precio = 20 * peso_kilogramo

mensaje = (f'''
    Monto a pagar: {internacional_precio or peso_kilogramo}
    Destino: {tipo_destino}
    Nombre del articulo: {nombre_articulo}
    Peso del articulo: {peso_kilogramo}
        ''')

if tipo_destino == 'nacional':
        print(mensaje)  

elif tipo_destino == 'internacional':
        print(mensaje)
  
elif peso_kilogramo <= 0 or tipo_destino != 'nacional' or 'internacional':
        print('El peso debe de ser mayor a 0 el destino solo puede ser (Nacional o Internacional)')
        