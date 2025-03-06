def sumaArgumentosVariables(*tuplas):
    try:
        sumaTotal = 0
        for i in tuplas:
            sumaTotal += i
        return sumaTotal
    except TypeError:
        return "SOLO SE PERMITEN NUMEROS NO PUENDEN CONTENER LETRAS"
        
print(sumaArgumentosVariables(5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5))