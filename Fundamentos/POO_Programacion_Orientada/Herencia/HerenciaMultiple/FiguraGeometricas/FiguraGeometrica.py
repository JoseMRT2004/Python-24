class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, value):
        if value <= 0:
            raise ValueError("El alto debe ser un valor positivo")
        self._alto = value
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, value):
        if value <= 0:
            raise ValueError("El ancho debe ser un valor positivo")
        self._ancho = value
    
    def CalcularArea(self):
        return self.alto * self.ancho
        
    def __str__(self):
        return f'''
    Ancho: {self.ancho}
    Alto: {self.alto}'''
    
class Color:
    def __init__(self, color):
        self.color = color
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El color debe ser una cadena no vacía")
        self._color = value
        
    def __str__(self):
        return f'''Color: {self.color}'''
    
    
class Cuadrado(FiguraGeometrica, Color):
        
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    @property
    def area(self):
        return self.CalcularArea()
    
    def __str__(self):
        return f'''
    {FiguraGeometrica.__str__(self)}
    Area: {self.CalcularArea()}
    {Color.__str__(self)}'''
  
if __name__ == '__main__':
    try:
        cuadro = Cuadrado(4, 5, "Rojo")
        print(f'''{cuadro}
            
    -_-_-_-_-_-_-_-_-_-_-_ Jerarquía de las Superclases _-_-_-_-_-_-_-_-_-_-_-_-_-_

    {Cuadrado.mro()}''')
    except (ValueError, AttributeError) as e:
        print(f"Error: {e}")
