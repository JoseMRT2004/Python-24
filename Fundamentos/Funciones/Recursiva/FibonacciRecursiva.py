def fibonacci_recursiva(numero):
    if numero <= 1:
        return numero
    else:
        fib1 = fibonacci_recursiva(numero - 1)
        fib2 = fibonacci_recursiva(numero - 2)
        result = fib1 + fib2
        return result

print(fibonacci_recursiva(10))
