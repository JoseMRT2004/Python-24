from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

def main():
    mi_biblioteca = Biblioteca()

    libro1 = Libro(Titulo="Cien años de soledad", Autor="Gabriel García Márquez", Isbn="9780060883287")
    libro2 = Libro(Titulo="1984", Autor="George Orwell", Isbn="9780451524935")
    libro3 = Libro(Titulo="El principito", Autor="Antoine de Saint-Exupéry", Isbn="9780156012195")

    mi_biblioteca.AgregarLibro(libro1)
    mi_biblioteca.AgregarLibro(libro2)
    mi_biblioteca.AgregarLibro(libro3)

    usuario1 = Usuario(Nombre="Juan Pérez", IdUsuario="001")
    usuario2 = Usuario(Nombre="Ana López", IdUsuario="002")

    mi_biblioteca.RegistrarUsuario(usuario1)
    mi_biblioteca.RegistrarUsuario(usuario2)

    print("Estado inicial de la biblioteca:")
    print(mi_biblioteca)

    print("\nPrestando libros:")
    mi_biblioteca.PrestarLibro("9780060883287", "U001")
    mi_biblioteca.PrestarLibro("9780451524935", "U002")

    print(usuario1)
    print(usuario2)
    print(libro1)
    print(libro2)

    print("\nDevolviendo libros:")
    mi_biblioteca.DevolverLibro("9780060883287", "U001")
    mi_biblioteca.DevolverLibro("9780451524935", "U002")

    print(usuario1)
    print(usuario2)
    print(libro1)
    print(libro2)

    print("\nEstado final de la biblioteca:")
    print(mi_biblioteca)

if __name__ == "__main__":
    main()
