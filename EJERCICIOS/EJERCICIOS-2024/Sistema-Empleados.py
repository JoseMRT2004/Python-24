decoracion = "*======================*"
mensaje =  "Sistemas De Empleados"

print(f'''
        {decoracion}
         {mensaje}
        {decoracion}\n''')

nombre_empleado = input('Nombre Del Empleado: ')
edad_empleado = int(input('Edad Del Empleado: '))
salario_empleado = float(input('Salario Del Empleado: '))
es_jefe_departamento = input('Eres Jefe Departamento (Si/No): ')

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# Imprimir los valores del Empleado
print('\nDatos del Empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'Es Jefe de Departamento: {es_jefe_departamento}')
