class Persona:
    def __init__(self, ID='000', nombre='SIN NOMBRE ASIGNADO', edad=0):   
        self.ID = ID 
        self.nombre = nombre 
        self.edad = edad
        
    @classmethod
    def InicializarConNombreEdad(cls, nombre, edad):  # En teoria esto funcionaria como una SobreCarga del constructor 
        return cls(nombre=nombre, edad=edad)
    
    def MostrarLaInformacion(self):
         print(f'ID: {self.ID} Nombre: {self.nombre} Edad: {self.edad}')
         
         
if __name__ == '__main__':
         
    # Crear instancias de la clase Persona
    Persona1 = Persona(ID='001', nombre='Tomas Casas', edad=21)
    Persona2 = Persona(ID='002',nombre='Mariano Taveras', edad=25)
    persona3 = Persona()  # Constructor por defecto
    persona4 = Persona.InicializarConNombreEdad('Ramon Emilio', 30)

    Persona1.MostrarLaInformacion()
    Persona2.MostrarLaInformacion() 
    persona3.MostrarLaInformacion()
    persona4.MostrarLaInformacion()
