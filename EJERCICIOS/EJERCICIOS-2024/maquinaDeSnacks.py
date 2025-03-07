'''
1. Crear un programa donde los usuarios podrán comprar snacks de una lista inicial.
2. Cada snack tiene un ID, un nombre y su precio.
3. Para comprar un snack, se debe indicar el ID del snack a comprar y se debe agregar a una lista de productos comprados.
4. Mostrar el ticket de venta final con el total de productos comprados y el total de la venta.

   - Nota: Use [POO] para practicar pero no es obligatorio

'''


import os

class Snack:
    def __init__(self, snack_id, nombre, precio):
        self.snack_id = snack_id
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.snack_id}. {self.nombre} - ${self.precio:.2f}"

class MaquinaDeSnacks:
    def __init__(self):
        self.snacks = [
            Snack(1, "Papas", 1.50),
            Snack(2, "Chocolate", 2.00),
            Snack(3, "Refresco", 1.25),
            Snack(4, "Dulce", 0.75)
        ]
        self.carrito = []

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_snacks(self):
        print("Snacks disponibles:")
        for snack in self.snacks:
            print(snack)

    def agregar_al_carrito(self, snack_id):
        self.limpiar_pantalla()
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                self.carrito.append(snack)
                print(f"{snack.nombre} agregado al carrito.")
                return
        print("ID de snack no encontrado.")

    def mostrar_carrito(self):
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
        maquina.mostrar_snacks()
        eleccion = input("Ingresa el ID del snack para comprar - [ '#' para salir ]: ")
        if eleccion.lower() == '#':
            break
        try:
            snack_id = int(eleccion)
            maquina.agregar_al_carrito(snack_id)
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un ID de snack válido.")

    maquina.mostrar_carrito()

if __name__ == "__main__":
    main()
