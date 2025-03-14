class Atributos:
    __AtributosClass = 0  # Atributo de clase que funciona como contador

    def __init__(self, atributoObjeto):
        self.atributoObjeto = atributoObjeto  # Atributo de instancia
        Atributos.__AtributosClass += 1  

    @classmethod
    def get_contador(cls):
        return cls.__AtributosClass  # Método para acceder al contador
    
if __name__ == '__main__':

    p1 = Atributos('Instancia 1')
    p2 = Atributos('Instancia 2')
    p3 = Atributos('Instancia 3')

# Acceder al contador usando el método de clase
print(Atributos.get_contador()) 