from biblioteca import Biblioteca
from libro import Libro

bibliotecaNacional = Biblioteca('Biblioteca Nacional')
print(f'\n*** Bienvenidos a la {bibliotecaNacional.nombre} ***')

# Definicion de libros
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Ficción')
libro2 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Comedia')
libro3 = Libro('El amor en los tiempos del cólera', 'Gabriel García Márquez', 'Ficción')
libro4 = Libro('Pedro Páramo', 'Juan Rulfo', 'Ficción')
libro5 = Libro('Pantaleón y las visitadores', 'Mario Vargas Llosa', 'Comedia')

# Agregas los libros a la biblioteca
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

# Buscar libros por autor
autor = 'Gabriel García Márquez'
print(f'\nLibros de {autor}')
bibliotecaNacional.buscar_libros_por_autor(autor)

# Buscar libros por género
genero = 'Ficción'
print(f'\nLibros de {genero}')
bibliotecaNacional.buscar_libros_por_genero(genero)

# Mostrar todos los libros de la biblioteca
bibliotecaNacional.mostrar_todos_los_libros()