# Función main

# Solicitarle al usuario su edad.
# A continuación, solicitarle al usuario que ingrese 5 números y los almacene en un arreglo. A continuación pasarle ese arreglo como parámetro a una función llamada cálculos. 

#Funcion main 
def main():
    # solicita la edad al usuario 
    edad = int(input("Ingresa tu edad: "))
# Soliccitar al 5 nuemros y almacenalos en un arreglo 
    arreglo = []
    for i in range (5):
        numero = int(input(f"Ingresa el numero {i + 1 }: "))
        arreglo.append(numero)

    calculo(arreglo,edad)
# Lógica de la función calculos
# Debe recibir un arreglo de 5 valores y multiplicar cada elemento del arreglo por la edad del usuario e ir ingresando cada valor calculado en un nuevo arreglo. Ahí mismo debe pasarle el nuevo arreglo a otra función llamada total.
# Cuando reciba el resultado de la función total, debe pasárselo a otra función llamada verificacion. La funcion verificacion harás las acciones finales del programa.

def calculo(arreglo, edad):
    # Crear un nuevo arreglo con los valores 
    arreglo_multiplicado = [num * edad for num in arreglo ]
    
    total(arreglo_multiplicado, edad)

# Lógica de la función total:
# La funcion total debe recibir un arreglo de 5 números y calcular la sumatoria de los valores que sean mayor o igual que 100 y devolver / retornar ese valor a la funcion calculos.
def total(arreglo, edad):
    suma = sum(num for num in arreglo if num >= 100)
    
    verificacion(suma, edad)

# Lógica de la función verificación:
# Esta función debe recibir un valor y evaluar si este valor es mayor o igual que 500. Si es así, mostrar el mensaje "Valor alcanzado" 
# el número de veces de la edad del usuario, en caso contrario, mostrar el mensaje "valor insuficiente" solo una vez.

def verificacion(valor,edad):
    # si el valor es mayor o igual a 500
    if valor >= 500: 
        for _ in range(edad): # mostrar mensaje valor alcanzado
            print('Valor alcanzado')
    else:
            print(f'Valor insuficiente')
            
main()
        