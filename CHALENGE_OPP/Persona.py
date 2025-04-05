class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        self._edad = valor
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    def es_mayor(self):
        return self.edad >= 18
    
    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años"


# Instancias de Persona
p1 = Persona("Juan Pérez", 25)
p2 = Persona("Ana Gómez", 16)

print("--- Probando Persona ---")
print(p1)
print(p1.saludar())