print('*** Sistema de Inventarios ***')

inventario = []

numero_productos = int(input('Cuantos productos deseas agregar al inventario? '))

for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    # Creamos el diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# Mostrar el inventario inicial
print(f'\nInventario inicial: {inventario}')