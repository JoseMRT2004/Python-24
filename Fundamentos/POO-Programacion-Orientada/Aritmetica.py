'''
Ejercicio: Creación de la Clase Aritmética

- Definir la Clase Aritmética:
   - Crear la clase Aritmetica
   - Agregar dos atributos:
     - ooperando1: un valor de tipo entero
     - ooperando2: un valor de tipo entero
- Agregar los siguientes métodos:
     - sumar: suma los dos operandos
     - restar: resta el segundo operando del primero
     - multiplicar: multiplica los dos operandos
     - dividir: divide el primer operando por el segundo, comprobando que el divisor no sea cero
     '''

     
class Aritmetica:
    def __init__(self,operador1,operador2):
        self.operando1 = operador1
        self.operando2 = operador2
        
    def suma(self):
                return self.operando1 + self.operando2
            
    def resta(self):
                return self.operando1 - self.operando2
            
    def multiplica(self):
                return self.operando1 * self.operando2
            
    def ponencia(self):
                return self.operando1 ** self.operando2
            
    def divide(self):
              if self.operando2 != 0:
                 return self.operando1 / self.operando2
              else:
                 return "Error: División por cero"
             
             
             
if __name__ == '__main__': # Si tu estas aquí, se ejecuta, si no lo hace. The end 
            
    # Creación del primer objeto
    aritmetica1 = Aritmetica(5, 3)

    output = f'''
    Suma: {aritmetica1.suma()}
    Resta: {aritmetica1.resta()}
    Muntiplicacion: {aritmetica1.multiplica()}
    Divicion: {aritmetica1.divide()}
    Pontenciacion: {aritmetica1.ponencia()}
    '''

    print(output)

'''
Explicacion teorica tecnica: 

La construcción if __name__ == '__main__': 
es muy útil para asegurar que cierto código solo se ejecute 
cuando el script se ejecuta directamente,
no cuando se importa como un módulo en otro script.'''