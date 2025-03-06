# Definición de una función con argumentos
def saludar(nombre, edad):
    if not isinstance(edad, int):
        print("Error: La edad debe ser un número entero.")
        return
    
    if not isinstance(nombre, str):
        print("Error: El nombre debe ser una cadena de texto.")
        return
    
    print(f"Hola {nombre}, tienes {edad} años.")
    
    if edad < 18:
        print("Eres menor de edad.")
    elif edad < 65:
        print("Eres un adulto.")
    else:
        print("Eres una persona mayor.")

saludar("Maria", 24)
