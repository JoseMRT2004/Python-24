class Persona:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre
    
    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad: int):
        self._edad = nueva_edad
    
    def saludar(self) -> str:
        return f"Hola, soy {self._nombre}"
    
    def es_mayor(self) -> bool:
        return self._edad >= 18

    def __str__(self):
        return f'''nombre: {self.nombre}   
edad: {self.edad} 
'''


p = Persona("Juan Pérez", 25)
print(p)
print(p.saludar())      
print(p.es_mayor())    
p.edad = 17
print(p.es_mayor())    

