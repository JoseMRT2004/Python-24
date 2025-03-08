# Crea una clase persona que tenga los atributos nombre y edad 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
        
    
        
    def MostrarLaInformacion(self):
         print(f'''{self.nombre} - {self.edad}''')
         
         
Persona1 = Persona(nombre='Tomas Casas',edad=21)
Persona2 = Persona(nombre='Ramon Taveras',edad=22)
Persona3 = Persona(nombre='Mariano Taveras',edad=25)


Persona1.MostrarLaInformacion()
Persona2.MostrarLaInformacion()
Persona3.MostrarLaInformacion()
