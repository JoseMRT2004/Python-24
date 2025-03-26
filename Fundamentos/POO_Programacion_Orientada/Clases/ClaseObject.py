class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribir el metodo __str__
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}'''

persona1 = Persona('Ana', 'Martinez')
print(persona1) # El metodo __str__ se llama automaticamente desde print
#print(persona1.__str__()) esto es opcional