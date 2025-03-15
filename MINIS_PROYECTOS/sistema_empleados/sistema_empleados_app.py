from empleado import Empleado
from empresa import Empresa


if __name__ == "__main__":

      print(f'''                     
                  *** Sistema de Empleados *** ''')

      empresa1 = Empresa('Global Mentoring')

      empresa1.contratar_empleado('Juan', 'Ventas')
      empresa1.contratar_empleado('María', 'Marketing')
      empresa1.contratar_empleado('Pedro', 'Ventas')
      empresa1.contratar_empleado('Ana', 'Recursos Humanos')

      print(f'''
            
            - Total de empleados: {Empleado.obtener_total_empleados()}
            - Empleados en el departamento de Ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}

      ''')


      empresa1.obtener_total_empleados()