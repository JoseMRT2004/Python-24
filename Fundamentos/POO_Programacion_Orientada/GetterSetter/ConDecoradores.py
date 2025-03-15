class Arbol:
    def __init__(self, especie='Sin Asignar', edad='Sin Asignar', alturaMetros='Sin Asignar'):
        self._especie = especie
        self._edad = edad
        self._alturaMetros = alturaMetros

    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, especie):
        self._especie = especie

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def alturaMetros(self):
        return self._alturaMetros

    @alturaMetros.setter
    def alturaMetros(self, alturaMetros):
        self._alturaMetros = alturaMetros

    def descripcionDelArbol(self):
        print(f'''
          - Árboles Descripcion -

            Especie: {self._especie}
            Edad: {self._edad}
            Altura en Metros: {self._alturaMetros}''')


if __name__ == '__main__':
    Arbol1 = Arbol('Roble', '50 años', '15 metros')
    Arbol1.descripcionDelArbol()
    
    Arbol1.especie = 'Eucalipto'
    Arbol1.edad = '40 años'
    Arbol1.alturaMetros = '30 metros'
    Arbol1.descripcionDelArbol()
    