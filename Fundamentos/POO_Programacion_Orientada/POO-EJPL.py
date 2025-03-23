class Computadora:
    def __init__(self, marca, modelo, ram, almacenamiento, procesador, tarjetaGrafica):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.procesador = procesador
        self.tarjetaGrafica = tarjetaGrafica

    def __str__(self):
        return f'''
        Marca: {self.marca}
        Modelo: {self.modelo}
        RAM: {self.ram} GB
        Almacenamiento: {self.almacenamiento} GB
        Procesador: {self.procesador}
        Tarjeta Gráfica: {self.tarjetaGrafica}
        '''


class Celular(Computadora):
    def __init__(self, marca, modelo, ram, almacenamiento, procesador, camara):
        super().__init__(marca, modelo, ram, almacenamiento, procesador, tarjetaGrafica="No aplica")
        self.camara = camara

   


celular1 = Celular("iPhone", "15 Pro Max", 16, 1024, "Apple A17 Pro", 48)
computadora1 = Computadora("Dell", "XPS 15", 16, 512, "Intel Core i7", "NVIDIA GTX 1650")

print(f'''{celular1}
        -------------------------------
{computadora1}''')
