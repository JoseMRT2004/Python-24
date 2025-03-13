class Aritmetica:
    def __init__(self, operador1=None, operador2=None):
        self.__operando1 = operador1
        self.__operando2 = operador2

    @property
    def operando1(self):
        return self.__operando1


    @property
    def operando2(self):
        return self.__operando2

    @property
    def suma(self):
        return self.__operando1 + self.__operando2

    @property
    def resta(self):
        return self.__operando1 - self.__operando2

    @property
    def multiplica(self):
        return self.__operando1 * self.__operando2

    @property
    def divide(self):
        if self.__operando2 != 0:
            return self.__operando1 / self.__operando2
        else:
            return "Error: División por cero"

    @property
    def potencia(self):
        return self.__operando1 ** self.__operando2

    @operando2.setter
    def operando2(self, valor):
        self.__operando2 = valor

    @operando1.setter
    def operando1(self, valor):
        self.__operando1 = valor

if __name__ == '__main__':
    
    aritmetica1 = Aritmetica(5, 3)
    aritmetica2 = Aritmetica()
    
    aritmetica2.operando1 = 45
    aritmetica2.operando2 = 5
    aritmetica1.operando2 = 5
    
    

    output = f'''
    Suma: {aritmetica2.suma}
    Resta: {aritmetica1.resta}
    Multiplicacion: {aritmetica2.multiplica}
    Division: {aritmetica1.divide}
    Potenciacion: {aritmetica1.potencia}
    '''

    print(output)