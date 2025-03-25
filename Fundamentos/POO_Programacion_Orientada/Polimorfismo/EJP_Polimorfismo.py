class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

print('*** Ejemplo Polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
animal1.hacer_sonido()

print('\nClase Hija Perro: ')
perro1 = Perro()
perro1.hacer_sonido()  

print('\nClase Hija Gato: ')
gato1 = Gato()
gato1.hacer_sonido()