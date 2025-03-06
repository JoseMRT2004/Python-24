# Cuenta atrás de forma recursiva

def contador(numero):
    if numero < 0:
        return
    print(numero)
    contador(numero - 1)

contador(10)
