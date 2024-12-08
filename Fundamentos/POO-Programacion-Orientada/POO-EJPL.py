class celulares(object):
    def __init__(self, marca, modelo, ram, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.almacenamiento = almacenamiento
    
    def info_producto(self):
        info = f'''
        Marca: {self.marca}
        Modelo: {self.modelo}
        RAM: {self.ram} GB
        Almacenamiento: {self.almacenamiento} GB
        '''
        return info

class computadoras(celulares):
    def __init__(self, marca, modelo, ram, almacenamiento, procesador, tarjeta_grafica):
        super().__init__(marca, modelo, ram, almacenamiento)
        self.procesador = procesador
        self.tarjeta_grafica = tarjeta_grafica
    
    def info_producto(self):
        info = super().info_producto()
        info += f'''
        Procesador: {self.procesador}
        Tarjeta Gráfica: {self.tarjeta_grafica}
        '''
        return info

computadora1 = computadoras("Dell", "XPS 15", 16, 512, "Intel core i7", "NVIDIA GTX 1650")
celulares1 = celulares("Iphone", "15 PRO Max", 16, 1024 )


print(f'''{computadora1.info_producto()}
        -------------------------------
{celulares1.info_producto()}''')


