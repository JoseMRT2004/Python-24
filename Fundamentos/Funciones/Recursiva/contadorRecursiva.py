# Contador de forma recurvisa 

def contadorRecursivo(numero):
    if numero == 1: 
        print(numero, end=' ')
    else:
        contadorRecursivo(numero - 1)
        print(numero, end=' ')
        

contadorRecursivo(10)