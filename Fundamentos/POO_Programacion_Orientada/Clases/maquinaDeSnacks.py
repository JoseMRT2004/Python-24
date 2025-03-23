'''
1. Crear un programa donde los usuarios podrán comprar snacks de una lista inicial.
2. Cada snack tiene un ID, un nombre y su precio.
3. Para comprar un snack, se debe indicar el ID del snack a comprar y se debe agregar a una lista de productos comprados.
4. Mostrar el ticket de venta final con el total de productos comprados y el total de la venta.

   - Nota: Use [POO] para practicar pero no es obligatorio

'''


import os

class Snack:
    def __init__(self, snackID, nombre, precio):
        self.snackID = snackID
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'''ID: {self.snackID} {self.nombre} → ${self.precio:.2f}'''

class MaquinaDeSnacks:
    def __init__(self):
        self.snacks = [
            Snack(1, "Papas", 1.50),
            Snack(2, "Chocolate", 2.00),
            Snack(3, "Refresco", 1.25),
            Snack(4, "Dulce", 0.75)
        ]
        self.carrito = []

    def limpiarPantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrarSnacks(self):
        print("Snacks disponibles:")
        for snack in self.snacks:
            print(snack)

    def agregarAlCarrito(self, snackID):
        self.limpiarPantalla()
        for snack in self.snacks:
            if snack.snackID == snackID:
                self.carrito.append(snack)
                return
        print("ID de snack no encontrado.")

    def mostrarCarrito(self):
        if not self.carrito:
            print("Tu carrito está vacío.")
            return

        print("Tu carrito:")
        total = 0
        for snack in self.carrito:
            print(snack)
            total += snack.precio
        print(f"Total: ${total:.2f}")

def main():
    maquina = MaquinaDeSnacks()
    
    while True:
        maquina.mostrarSnacks()
        
        eleccion = input("Ingresa el ID del snack para comprar - [ '#' para salir ]: ")
        if eleccion.lower() == '#':
            break
        try:
            snackID = int(eleccion)
            maquina.agregarAlCarrito(snackID)
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un ID de snack válido.")

    maquina.mostrarCarrito()

if __name__ == "__main__":
    main()
