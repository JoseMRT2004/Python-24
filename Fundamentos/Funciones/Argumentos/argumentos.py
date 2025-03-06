# Definición de una función con argumentos
def saludar(nombre, edad):
    # Verifica si la edad es un número entero
    if not isinstance(edad, int):
        print("Error: La edad debe ser un número entero.")
        return
    
    # Verifica si el nombre es una cadena de texto
    if not isinstance(nombre, str):
        print("Error: El nombre debe ser una cadena de texto.")
        return
    
    # Imprime un saludo con el nombre y la edad
    print(f"Hola {nombre}, tienes {edad} años.")
    
    # Determina la categoría de edad de la persona
    if edad < 18:
        print("Eres menor de edad.")
    elif edad < 65:
        print("Eres un adulto.")
    else:
        print("Eres una persona mayor.")

# Llama a la función saludar con los argumentos "Maria" y 24
saludar("Maria", 24)
