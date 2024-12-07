print('Creación y Validación de un Password ***')

password = input('Ingresa un password (debe tener al menos 6 caracteres: ')

while len(password) < 6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres')
    password = input('Ingresa un nuevo valor de password: ')
else:
    print('El valor de password es válido')
