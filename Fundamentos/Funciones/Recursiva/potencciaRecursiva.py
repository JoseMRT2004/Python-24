# Calcula de forma recursiva la exponente de un base 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)
    
print(potencia(base=4,exponente=5))