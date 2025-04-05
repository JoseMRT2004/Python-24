from Persona import Persona  

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, matricula):
        super().__init__(nombre, edad)
        self._carrera = carrera
        self._matricula = matricula  

    @property
    def carrera(self):
        return self._carrera
    
    @carrera.setter
    def carrera(self, valor):
        self._carrera = valor
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, valor):
        self._matricula = valor
    
    def __str__(self):
        return f'''Estudiante:
Nombre: {self.nombre}
Edad: {self.edad}
Carrera: {self.carrera}
Matrícula: {self.matricula}'''

e1 = Estudiante("Carlos Ruiz", 20, "Medicina", "M2023001")


print("--- Probando Estudiante ---")
print(e1)
print(e1.saludar())
