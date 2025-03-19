class Usuario:
    def __init__(self, Nombre="Desconocido", IdUsuario="0000"):
        self._Nombre = Nombre
        self._IdUsuario = IdUsuario
        self._LibrosPrestados = []

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre

    @property
    def IdUsuario(self):
        return self._IdUsuario

    @IdUsuario.setter
    def IdUsuario(self, IdUsuario):
        self._IdUsuario = IdUsuario

    @property
    def LibrosPrestados(self):
        return self._LibrosPrestados

    @LibrosPrestados.setter
    def LibrosPrestados(self, LibrosPrestados):
        self._LibrosPrestados = LibrosPrestados

    def PrestarLibro(self, Libro):
        if Libro.Prestar():
            self._LibrosPrestados.append(Libro)

    def DevolverLibro(self, Libro):
        if Libro in self._LibrosPrestados:
            Libro.Devolver()
            self._LibrosPrestados.remove(Libro)

    def __str__(self):
        Libros = ", ".join(Libro.Titulo for Libro in self._LibrosPrestados) or "Ninguno"
        return f"Usuario: {self._Nombre} | ID: {self._IdUsuario} | Libros Prestados: {Libros}"
