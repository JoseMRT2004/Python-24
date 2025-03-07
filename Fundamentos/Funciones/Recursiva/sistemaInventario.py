import os

'''Sistema de inventario con funciones:
    1. Mostrar un menú con las siguientes opciones:
            a. Mostrar el inventario.
            b. Agregar un nuevo producto.
            c. Buscar un producto por ID.
            d. Salir del sistema.
    2. Cada producto en el inventario tendrá los siguientes atributos:
            a. ID
            b. Nombre
            c. Precio
            d. Cantidad en el inventario'''
        

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

menu = '''
======================================
======= Sistema de inventario ========
======================================
  
 [ 1 ] - Mostrar el inventario.
 [ 2 ] - Agregar un nuevo producto.
 [ 3 ] - Buscar un producto por ID.
 [ 4 ] - Salir del sistema.
      
      '''
  
listProducto = []

def mostrarMenu():
    print(menu)


def agregarProducto(**argumentosProducto):
    listProducto.append(argumentosProducto)

def mostrarInventario():
    for i, producto in enumerate(listProducto, start=1):
        print(f"{i} - {producto}")

def buscarProductoID(id):
    for producto in listProducto:
        if producto['ID'] == id:
            return producto

def salirDelSistema():
    print('Saliendo del sistema...')
    exit()

def opcionNoValida():
    print('Opción no válida, por favor intenta de nuevo.')

if __name__ == "__main__":
    def main():
        while True:
            mostrarMenu()
            opcion = int(input(' Ingresa La opcion Deseada → '))
            
            if opcion == 1:
                limpiarPantalla()
                mostrarInventario()
            elif opcion == 2:
                limpiarPantalla()
                agregarProducto(
                    ID=input('Ingresa el ID del producto: '),
                    Nombre=input('Ingresa el nombre del producto: '),
                    Precio=float(input('Ingresa el precio del producto: ')),
                    Cantidad=int(input('Ingresa la cantidad del producto: '))
                )
            elif opcion == 3:
                limpiarPantalla()
                print(buscarProductoID(input('Ingresa el ID del producto a buscar: ')) or
                    'Producto no encontrado.')
            elif opcion == 4:
                salirDelSistema()
                limpiarPantalla()
            else:
                opcionNoValida()
                limpiarPantalla()
