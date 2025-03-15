class Usuario:
    __CONTADOR = 0  # Variable de clase para contar el número de usuarios

    def __init__(self, _nombre='NAME', _correo='SIN ASIGNAR CORREO', _estadoUser=True):
        self._nombre = _nombre
        self._correo = _correo
        self._estadoUser = _estadoUser

        
        if self._estadoUser: # Incrementa el contador solo si el usuario esta activo y asigna el id 
            Usuario.__CONTADOR += 1
            self.id = Usuario.__CONTADOR
        else:
            self.id = None  

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def estadoUser(self):
        return self._estadoUser

    @estadoUser.setter
    def estadoUser(self, estadoUser):
        self._estadoUser = estadoUser

    def informacionUsuario(self):
        return f'''
    -------------------------
     Nombre: {self._nombre}
     Correo: {self._correo}
     Estado: {"Activo" if self._estadoUser else "Inactivo"}
     ID: {self.id}
    -------------------------
        '''


if __name__ == '__main__':
    print(f'''
    Instancias En La Clase Usuario: {Usuario._Usuario__CONTADOR}
    ''')

    usuario1 = Usuario("Juan", "juan@example.com", )
    usuario2 = Usuario("Ana", "ana@example.com", _estadoUser=False)
    usuario3 = Usuario("Pedro", "pedro@example.com")
    usuario4 = Usuario("Maria", "maria@example.com")
    usuario5 = Usuario(_estadoUser=False)
    

    print(usuario1.informacionUsuario())
    print(usuario2.informacionUsuario())
    print(usuario3.informacionUsuario())
    print(usuario4.informacionUsuario())
    print(usuario5.informacionUsuario())
    

    print(f'''
    Instancias En La Clase Usuario: {Usuario._Usuario__CONTADOR}
    ''')