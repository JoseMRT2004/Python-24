# Inmutabilidad de cadenas en Python
cadena1 = "Hola mundo"  # Se asigna una cadena de texto a la variable 'cadena1'
cadena1 = "adios"  # 'cadena1' ahora apunta a una nueva cadena, la cadena original "Hola mundo" sigue siendo inmutable

nombre = "Jose"  # Se asigna el nombre "Jose" a la variable 'nombre'
edad = 23  # Se asigna el valor entero 23 a la variable 'edad'

apellidos = ["Taveras", "Reyes", "Perez", "Paniagua"]  # Lista de apellidos
Nombres = ["Jose", "Mariano", "Juan", "Leo"]  # Lista de nombres

# Concatenar texto con el método .join
listaNombres = " ".join(apellidos)  # Se usa .join para unir cada letra del apellido "Paniagua" separada por un espacio
print(cadena1[4])  # Imprime el carácter en la posición 4 de la cadena "adios", que es "s"
print(listaNombres)  # Imprime 'P a n i a g u a', ya que cada letra de "Paniagua" es separada por un espacio

# Concatenar texto con la función f-strings
NombresApellidos = f' {Nombres[0]} {apellidos[0]}'  # Combina el primer nombre y el primer apellido usando f-strings
print(f'Hola {nombre} tu edad es {edad}')  # Imprime el mensaje con el nombre y la edad utilizando f-strings

print(NombresApellidos)  # Imprime ' Jose Taveras', que es la combinación del primer nombre y apellido de las listas

print(f'Hola {nombre} tu edad es {edad}')  # Repite el mensaje con f-strings

# Concatenar texto con el método .format
print("Hola {} tu edad es {}".format(nombre, edad))  # Utiliza el método .format para insertar las variables 'nombre' y 'edad'
