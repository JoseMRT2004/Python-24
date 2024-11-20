print('\n*** Generador de Emails ***\n')

nombre_Completo = input('Nombre completo del usuario: ')

# Normaliza el nombre completo del usuario
nombre_normalizado = nombre_Completo.strip()
nombre_normalizado = nombre_normalizado.replace(' ', '.')
nombre_normalizado = nombre_normalizado.lower()

# Muestra el nombre normalizado
print(f'Nombre normalizado: {nombre_normalizado}')

nombre_empresa = input('Nombre de la empresa: ')
extension_dominio = input('Extensión del dominio (DO) (MX): ')

print(f'Nombre Empresa Normalizado: {extension_dominio}')

# Normaliza el dominio del email
dominio_normalizado = f'.{extension_dominio}'.strip().replace(' ', '.').lower()
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{dominio_normalizado}'

# Muestra el dominio normalizado
print(f'Dominio del email normalizado: {dominio_email_normalizado}')

# Genera el email final
email = f'{nombre_normalizado}{dominio_email_normalizado}'

print(f'''
FELICIDADES!!! ahora tienes un email corporativo con el siguiente formato:
      
      Email final generado: {email}''')
