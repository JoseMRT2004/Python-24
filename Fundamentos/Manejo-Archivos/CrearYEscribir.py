try:
    with open('Fundamentos/Manejo-Archivos/Test2.txt', 'w') as file:
        file.write("Solo estoy probando que escribe en el archivo")
except FileNotFoundError as e:
    print(f"Error: {e}")
    