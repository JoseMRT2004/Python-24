from POO_Programacion_Orientada.Sistema_Empleados import Empleado

class Empresa:
    
    def __init__(self, _nameEmpresa,):
        self._nameEmpresa = _nameEmpresa
        self.listEmpleados = []
        
    def contratarEmpleados(self,name,lastName,email,departamento):
        empleado = empleado(name,lastName,email,departamento)
        self.listEmpleados.append(Empleado)
        
    def empleadosPorDepartamento(self,departamento):
        TotalaEmpleadosPorDepartamento = 0
        for empleado in self.listEmpleados:
           if empleado.departamento  == departamento:
                TotalaEmpleadosPorDepartamento += 1
        return TotalaEmpleadosPorDepartamento
               