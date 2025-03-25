# Polimorfismo
class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    # pass
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

# Funcion polimorfica
def hacer_sonido_animal(animal):  # duck typing
    animal.hacer_sonido()

print('*** Ejemplo Polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
hacer_sonido_animal(animal1)
# Definimos un objeto de la clase Perro
print('\nClase Hija Perro: ')
perro1 = Perro()
hacer_sonido_animal(perro1)
# Definimos un objeto de la clase Gato
print('\nClase Hija Gato: ')
gato1 = Gato()
hacer_sonido_animal(gato1)