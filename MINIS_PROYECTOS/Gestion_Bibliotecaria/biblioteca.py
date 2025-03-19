class Biblioteca:
    def __init__(self):
        self._Libros = []
        self._Usuarios = []

    @property
    def Libros(self):
        return self._Libros

    @Libros.setter
    def Libros(self, Libros):
        self._Libros = Libros

    @property
    def Usuarios(self):
        return self._Usuarios

    @Usuarios.setter
    def Usuarios(self, Usuarios):
        self._Usuarios = Usuarios

    def AgregarLibro(self, Libro):
        self._Libros.append(Libro)

    def RegistrarUsuario(self, Usuario):
        self._Usuarios.append(Usuario)

    def PrestarLibro(self, Isbn, IdUsuario):
        Libro = next((L for L in self._Libros if L.Isbn == Isbn and L.Disponible), None)
        Usuario = next((U for U in self._Usuarios if U.IdUsuario == IdUsuario), None)

        if Libro and Usuario:
            Usuario.PrestarLibro(Libro)

    def DevolverLibro(self, Isbn, IdUsuario):
        Usuario = next((U for U in self._Usuarios if U.IdUsuario == IdUsuario), None)

        if Usuario:
            Libro = next((L for L in Usuario.LibrosPrestados if L.Isbn == Isbn), None)
            if Libro:
                Usuario.DevolverLibro(Libro)

    def __str__(self):
        return f"Biblioteca: {len(self._Libros)} libros | {len(self._Usuarios)} usuarios"
