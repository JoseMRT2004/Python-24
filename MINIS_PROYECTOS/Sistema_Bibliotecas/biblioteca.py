class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_libros_por_autor(self, autor):
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)

    def buscar_libros_por_genero(self, genero):
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_los_libros(self):
        print(f'\nTodos los libros de la biblioteca {self._nombre}')
        for libro in self._libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self, libro):
        print(f'Libro -> Título: {libro.titulo}, Autor: {libro._autor}, '
              f'Género: {libro.genero}')

    @property
    def nombre(self):
        return self._nombre

    @property
    def libros(self):
        return self._libros