class Persona:
    def __init__(self, ID='000', nombre='SIN NOMBRE ASIGNADO', edad=0):   
        self.ID = ID 
        self.nombre = nombre 
        self.edad = edad
        
    @classmethod
    def InicializarConNombreEdad(cls, nombre, edad):  
        return cls(nombre=nombre, edad=edad)
    
    def __str__(self):
         return f'''
     ID: {self.ID} 
     Nombre: {self.nombre}
     Edad: {self.edad}'''
         
         
if __name__ == '__main__':
         
    Persona1 = Persona(ID='001', nombre='Tomas Casas', edad=21)
    Persona2 = Persona(ID='002',nombre='Mariano Taveras', edad=25)
    persona3 = Persona()  
    persona4 = Persona.InicializarConNombreEdad('Ramon Emilio', 30)

print(f'''
      
    {Persona1}
    {Persona2} 
    {persona3}
    {persona4}
    
''')