'''
Python, como casi todos los lenguajes de programación, tiene una clase de excepciones 
que tiene a su vez sub-clases específicas. La intención de estas es manejar 
excepciones en el código - errores previstos por el desarrollador del software.
'''

# ! Existen exepciones espefificas para situasiones ya previstas y estas la exepcion que yo llamo de uso general-no-usar-sin-verificar-su-utilidad en ese contexto:

# 1️⃣ - ValueError: ocurre cuando un tipo de dato no es válido para una operación
try:
    edad = int("veinte")  # cadena no convertible a entero
except ValueError:
    print("Error: Debes ingresar un número válido.")

# 2️⃣ - ZeroDivisionError: división por cero, no permitida matemáticamente
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División entre cero.")

# 3️⃣ - FileNotFoundError: cuando se intenta abrir un archivo que no existe
try:
    with open("archivo.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")

# 4️⃣ - TypeError: cuando se realiza una operación entre tipos incompatibles
try:
    suma = "texto" + 5  # no se puede sumar str con int
except TypeError:
    print("Error: Tipos incompatibles en operación.")

# 5️⃣ - IndexError: acceso a una posición inválida en una lista
try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Error: Índice fuera del rango de la lista.")

# 6️⃣ - Uso peligroso de Exception (no recomendado sin verificar)
try:
    numero = int("texto")
except Exception as error:
    print("Ocurrió un error:", error)  # Demasiado genérico
