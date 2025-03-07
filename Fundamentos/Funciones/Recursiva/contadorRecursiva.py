# Contador de forma recurvisa 

def contadorRecursivo(numero):
    if numero == 1: 
        print(numero)
    else:
        contadorRecursivo(numero - 1)
        print(numero)
        

contadorRecursivo(10)