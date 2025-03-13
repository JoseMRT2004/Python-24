class Animal:
    def __init__(self, raza='Sin Asignar', edadMeses='Sin Asignar', pesoKg='Sin Asignar'):
        self._raza = raza
        self._edadMeses = edadMeses
        self._pesoKg = pesoKg

    def getRaza(self):
        return self._raza

    def getEdad(self):
        return self._edadMeses

    def getPesoKg(self):
        return self._pesoKg

    def setRaza(self, raza):
        self._raza = raza

    def setEdad(self, edadMeses):
        self._edadMeses = edadMeses

    def setPesoKg(self, pesoKg):
        self._pesoKg = pesoKg

    def descripcionDelAnimal(self):
        print(f'''
          - Animales Disponibles Descripcion -

            Raza: {self._raza}
            Edad: {self._edadMeses} meses
            Peso: {self._pesoKg} kg''')


if __name__ == '__main__':
    Animal1 = Animal('Chihuahua', '12', '5')
    Animal2 = Animal('Labrador', '24', '30')
    Animal3 = Animal('Bulldog', '36', '25')

    Animal1.descripcionDelAnimal()
    Animal2.descripcionDelAnimal()
    Animal3.descripcionDelAnimal()

    Animal1.setRaza('Chihuahua')
    Animal1.setEdad('14')
    Animal1.setPesoKg('6')

    print("\nDespués de modificar los atributos de Animal1:")
    Animal1.descripcionDelAnimal()