# Crea una función que devuelva el factorial de un número 

def factorial(numero):
    if numero == 1:
        return 1
    return numero * factorial(numero - 1)
    
    
print(factorial(10))