'''La clase se va a llamar Coche y vamos a empezar a agregar la definición de nuestra clase 
     - Usa la encapsulacion
     - getter - setter'''
     
class Coche:
    def __init__(self, marca='Sin Asignar', modelo='Sin Asignar', color='Sin Asignar'):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_color(self):
        return self.__color

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_color(self, color):
        self.__color = color

    def conducir(self):
        print(f'''
          - Conduciendo el Coche -

            Marca: {self.__marca}
            Modelo: {self.__modelo}
            Color: {self.__color}''')


if __name__ == '__main__':
    coche1 = Coche('Volvo', 'Z300', 'Azul')
    coche2 = Coche('Toyota', 'Corolla', 'Rojo')
    coche3 = Coche('Ford', 'Mustang', 'Blanco')

    coche1.set_marca('Bugatti')
    coche1.set_modelo('Chiron')
    coche1.set_color('Negro')

    coche1.conducir()
    coche2.conducir()
    coche3.conducir()