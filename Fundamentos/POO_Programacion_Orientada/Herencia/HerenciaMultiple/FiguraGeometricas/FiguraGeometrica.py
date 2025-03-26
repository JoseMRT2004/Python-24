''' ¡Al estar trabajando en un directorio tan profundo, prefiero hacerlo así para tener todo más organizado,
pero estas clases deberían estar en módulos individuales!'''


class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        
    def CalcularArea(self):
        return self.alto * self.ancho
        
    def __str__(self):
        return f'''
    Ancho: {self.ancho}
    Alto: {self.alto}'''
    
class Color:
    def __init__(self, color):
        self.color = color
        
    def __str__(self):
        return f'''Color: {self.color}'''
    
    
class Cuadreado(FiguraGeometrica, Color):
        
    def __init__(self, alto, ancho, area, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        self.area = area
        
    def __str__(self):
        return f'''
    {super().__str__()}
    Area: {cuadro.CalcularArea()}
    {Color.__str__(self)}'''
    
cuadro = Cuadreado(4, 5, 20, "Rojo")
print(f'{cuadro}')
