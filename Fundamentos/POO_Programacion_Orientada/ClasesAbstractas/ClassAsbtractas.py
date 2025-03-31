from abc import ABC, abstractmethod

class Instrumentos(ABC):
    def __init__(self, categoria: str):
        self.categoria = categoria

    @abstractmethod
    def descripcion(self) -> str:
        pass

class Instrumento(Instrumentos):
    def __init__(self, categoria: str, nombre: str):
        super().__init__(categoria)
        self.nombre = nombre

    @abstractmethod
    def obtener_info(self) -> str:
        pass

    def descripcion(self) -> str:
        return f"Instrumento de la categoría: {self.categoria}"

class Cuerda(Instrumento):
    def obtener_info(self) -> str:
        return f"Instrumento de cuerda: {self.nombre}"

class Percusion(Instrumento):
    def obtener_info(self) -> str:
        return f"Instrumento de percusión: {self.nombre}"

class Viento(Instrumento):
    def obtener_info(self) -> str:
        return f"Instrumento de viento: {self.nombre}"

guitarra = Cuerda("Cuerda", "Guitarra")
bateria = Percusion("Percusión", "Batería")
flauta = Viento("Viento", "Flauta")

print(f'''

    {guitarra.descripcion()} - {guitarra.obtener_info()}
    {bateria.descripcion()} - {bateria.obtener_info()}
    {flauta.descripcion()} - {flauta.obtener_info()}
    Jerarquia de Clases: Clases - {Instrumento.mro()}

''')
