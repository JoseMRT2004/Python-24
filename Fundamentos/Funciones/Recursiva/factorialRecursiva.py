# Crea una función que devuelva el factorial de un número y lo formatee con comas

def calcularFactorial(numero):
    def factorial(numero):
        if numero == 1 or numero == 0:
            return 1
        return numero * factorial(numero - 1)
    
    resultado = factorial(numero)
    resultado_formateado = "{:,}".format(resultado)
    return resultado_formateado

numero = 10

print(calcularFactorial(numero))
