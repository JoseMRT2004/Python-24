import os 

print('''\n=====================================================
Introduce números al array. Escribe '.' para terminar  
=====================================================\n''')
numeros = []

while True:
    entrada = input("Número (o '.' para terminar): ")
    if entrada == '.':
        break
    try:
        numeros += [float(entrada)]  # Usamos += para agregar un número como un elemento de lista
    except ValueError:
        print("Entrada inválida. Asegúrate de introducir un número.")

if numeros:
    minimo = numeros[0]
    maximo = numeros[0]

    for num in numeros:
        if num < minimo:
            minimo = num
        elif num > maximo:
            maximo = num
            
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f''' Resultados:\n
 - Número mínimo: {minimo}
 - Número máximo: {maximo}\n''')
else:
    print("No se ingresaron números. Operación terminada.")