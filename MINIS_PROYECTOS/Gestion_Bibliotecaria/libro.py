class Libro:
    def __init__(self, Titulo="Sin título", Autor="Desconocido", Isbn="0000000000000", Disponible=True):
        self._Titulo = Titulo
        self._Autor = Autor
        self._Isbn = Isbn
        self._Disponible = Disponible

    def Prestar(self):
        if self._Disponible:
            self._Disponible = False
            return True
        return False

    def Devolver(self):
        self._Disponible = True

    @property
    def Titulo(self):
        return self._Titulo

    @Titulo.setter
    def Titulo(self, Titulo):
        self._Titulo = Titulo

    @property
    def Autor(self):
        return self._Autor

    @Autor.setter
    def Autor(self, Autor):
        self._Autor = Autor

    @property
    def Isbn(self):
        return self._Isbn

    @Isbn.setter
    def Isbn(self, Isbn):
        self._Isbn = Isbn

    @property
    def Disponible(self):
        return self._Disponible

    @Disponible.setter
    def Disponible(self, Disponible):
        self._Disponible = Disponible

    def __str__(self):
        Estado = "Disponible" if self._Disponible else "No disponible"
        return f"{self._Titulo} - {self._Autor} | ISBN: {self._Isbn} | {Estado}"
