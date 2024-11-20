print('\n*** Generador de Emails ***\n')

nombre_Completo = input('Nombre completo del usuario: ')

# Nombre de usuario normalizado
nombre_normalizado = nombre_Completo.strip()
nombre_normalizado = nombre_normalizado.replace(' ', '.')
nombre_normalizado = nombre_normalizado.lower()

nombre_empresa = input('Nombre de la empresa: ')

extension_dominio = '.com.mx'
print(f'Extensión del dominio: {extension_dominio}')

# Nombre del Email normalizado
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'

print(f'Dominio del email normalizado: {dominio_email_normalizado}')

email = f'{nombre_normalizado}{dominio_email_normalizado}'
print(f'\nEmail final generado: {email}')
