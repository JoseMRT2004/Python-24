class Animal:
    def comer(self):
        print('Como muchas veces el día')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    # Sobreescritura del metodo dormir
    def dormir(self):
        print('Duermo 15 horas al día')

# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()  # Se llama el metodo sobreescrito de la clase hija
perro1.hacer_sonido()