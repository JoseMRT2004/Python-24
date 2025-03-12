'''La clase se va a llamar Coche y vamos a empezar a agregar la definición de nuestra clase 
     - Usa la encapsulacion
     - getter - setter'''
     
class Coche:
    def __init__(self, marca='Sin Asignar', modelo='Sin Asignar', color='Sin Asignar'):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_color(self):
        return self._color

    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_color(self, color):
        self._color = color

    def conducir(self):
        print(f'''
          - Conduciendo el Coche -

            Marca: {self._marca}
            Modelo: {self._modelo}
            Color: {self._color}''')


if __name__ == '__main__':
    coche1 = Coche('Volvo', 'Z300', 'Azul')
    coche2 = Coche('Toyota', 'Corolla', 'Rojo')
    coche3 = Coche('Ford', 'Mustang', 'Blanco')


    coche1.conducir()
    coche1.set_marca('Toyota')
    coche1.set_modelo('4Runner')
    coche1.set_color('Blanco')

    coche1.conducir()
    coche2.conducir()
    coche3.conducir()