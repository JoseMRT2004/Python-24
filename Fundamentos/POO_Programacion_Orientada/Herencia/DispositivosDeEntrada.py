class DispositivoEntrada:
    def __init__(self, marca, tipoEntrada):
        self.marca = marca
        self.tipoEntrada = tipoEntrada

    def __str__(self):
        return f"Marca: {self.marca} Tipo Entrada: {self.tipoEntrada}"


class Raton(DispositivoEntrada):
    contadorRatones = 0
    
    def __init__(self, marca, tipoEntrada):
        super().__init__(marca, tipoEntrada)
        Raton.contadorRatones += 1
        self.idRaton = Raton.contadorRatones
        
    def __str__(self):
        return f"Raton ID: {self.idRaton} {super().__str__()}"


class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    
    def __init__(self, marca, tipoEntrada):
        super().__init__(marca, tipoEntrada)
        Teclado.contadorTeclados += 1
        self.idTeclado = Teclado.contadorTeclados
        
    def __str__(self):
        return f"Teclado ID: {self.idTeclado} {super().__str__()}"


class Monitor:
    contadorMonitores = 0
    
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self.idMonitor = Monitor.contadorMonitores
        self.marca = marca
        self.tamaño = tamaño
        
    def __str__(self):
        return f"Monitor ID: {self.idMonitor} Marca: {self.marca} Tamaño: {self.tamaño}"


class Computadora:
    contadorComputadoras = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.idComputadora = Computadora.contadorComputadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
        
    def __str__(self):
        return f'''
    Computadora ID: {self.idComputadora}
    Nombre: {self.nombre}
    
    {self.monitor}
    {self.teclado}
    {self.raton}
    Ubicacion en la Memoria: {super().__str__()}'''


class Orden:
    contadorOrdenes = 0
    
    def __init__(self, computadoras=None):
        Orden.contadorOrdenes += 1
        self.idOrden = Orden.contadorOrdenes
        self.computadoras = computadoras if computadoras else []
        
    def agregarComputadora(self, computadora):
        self.computadoras.append(computadora)
        
    def __str__(self):
        computadoras_str = "\n".join(str(comp) for comp in self.computadoras)
        return f'''
    Orden ID: {self.idOrden}
    Computadoras:
    {computadoras_str}'''


if __name__ == "__main__":
    monitor1 = Monitor("Dell", "24 pulgadas")
    teclado1 = Teclado("Logitech", "USB")
    raton1 = Raton("HP", "Bluetooth")
    
    computadora1 = Computadora("Gamer Pro", monitor1, teclado1, raton1)
    
    orden1 = Orden()
    orden1.agregarComputadora(computadora1)
    
    print(orden1)