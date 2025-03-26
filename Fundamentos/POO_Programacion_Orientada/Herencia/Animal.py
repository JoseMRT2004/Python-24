class Animal: 
    def __init__(self, _color='NNNN', _edad=0, _pesoKg=0, _raza='NNNNN', __sonidoDelAnimal='NNNNNN'):
        self.__color = _color 
        self.__edad = _edad
        self.__pesoKg = _pesoKg
        self.__raza = _raza
        self.__sonidoDelAnimal = __sonidoDelAnimal  # Corrected the constructor parameter name
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    @property
    def pesoKg(self):
        return self.__pesoKg
    
    @pesoKg.setter
    def pesoKg(self, pesoKg):
        self.__pesoKg = pesoKg
    
    @property
    def raza(self):
        return self.__raza
    
    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @property
    def sonidoDelAnimal(self):  
        return self.__sonidoDelAnimal

    @sonidoDelAnimal.setter
    def sonidoDelAnimal(self, sonido): 
        self.__sonidoDelAnimal = sonido
    
    def __str__(self):
        return f'''
    Informacion del Animal:
     
        - Color: {self.color}
        - Edad: {self.edad}
        - Peso: {self.pesoKg}kg
        - Raza: {self.raza}
        - el animal esta {self.HacerSonido()}
        '''
    
    def Comer(self):
        return f'- el animal esta comiendo'
    
    def Dormir(self):
        return f'- el animal esta durmiendo'
    
    def HacerSonido(self):
        return f'el animal esta {self.__sonidoDelAnimal}'
    
class Perro(Animal):
    
    def __init__(self, _color, _edad, _pesoKg, _raza, __sonidoDelAnimal):
        super().__init__(_color, _edad, _pesoKg, _raza, __sonidoDelAnimal)
    
    def __str__(self):
        return super().__str__()
    
    def Dormir(self):
        return super().Dormir()
    
    def Comer(self):
        return super().Comer()
    
    def HacerSonido(self):
        return super().HacerSonido()

if __name__ == '__main__':
    
    perro = Perro('Blanco', 3, 15, 'Griego', 'Maullar')
    print(f'{perro}{perro.Dormir()}')
    
    perro.color = 'Negro'
    perro.edad = 4
    perro.pesoKg = 18
    perro.raza = 'Labrador'
    perro.__sonidoDelAnimal = 'Ladrar'  
    print(f'{perro}{perro.Comer()}')
