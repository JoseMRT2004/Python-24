class Empleados:
    
    __contadorEmpleados = 0
    
    def __init__(self,_name='NNNNN',_lastName='NNNNN',_email='NNNNN',_departamento='NNNNNN'):
        self._name = _name
        self._lastName = _lastName
        self._email = _email
        self._departemento = _departamento
        Empleados.__contadorEmpleados += 1
        self.id = Empleados.__contadorEmpleados
        
    @classmethod
    def EmpleadosTotal(cls):
       return cls.__contadorEmpleados
   
   
   
   
   
        
        
    