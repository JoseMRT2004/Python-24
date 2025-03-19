# Ejercicios de Programación Orientada a Objetos (POO) en Python

Este repositorio contiene una lista de ejercicios para practicar y dominar los conceptos de Programación Orientada a Objetos (POO) en Python. Los ejercicios están organizados en tres niveles de dificultad: Principiante, Intermedio y Avanzado, con 15 ejercicios en cada nivel. Además, se incluye un ejercicio Bonus al final, que es un desafío de lógica común en entrevistas de trabajo.

> - _Puedes resolver estos ejercicios en Python o en cualquier otro lenguaje de programación que prefieras. ¡El objetivo es aprender y practicar!_

---

### Nivel Principiante
- Ejercicios para familiarizarse con los conceptos básicos de POO en Python.

| Número | Descripción | Estado |
|---------|-------------|--------|
| 1  | Crear una clase `Persona` con atributos `nombre` y `edad`. |  |
| 2  | Agregar un método `saludar` que imprima "Hola, mi nombre es...". |  |
| 3  | Crear una instancia de `Persona` e imprimir sus atributos. |  |
| 4  | Definir un método `es_mayor_de_edad`. |  |
| 5  | Implementar un constructor `__init__` con valores por defecto. |  |
| 6  | Crear una subclase `Estudiante` que herede de `Persona`. |  |
| 7  | Agregar un atributo `carrera` a la clase `Estudiante`. |  |
| 8  | Sobreescribir el método `saludar` en `Estudiante`. |  |
| 9  | Crear una lista de objetos `Persona` y recorrerla. |  |
| 10 | Definir una clase `Coche` con atributos `marca` y `modelo`. |  |
| 11 | Agregar un método `acelerar` que cambie el estado del coche. |  |
| 12 | Implementar un método `frenar`. |  |
| 13 | Crear una clase `CuentaBancaria` con `saldo` y `depositar()`. |  |
| 14 | Implementar `retirar()` en `CuentaBancaria`. |  |
| 15 | Crear una instancia de `CuentaBancaria` y realizar operaciones. |  |

> ## Nivel Intermedio
> - Ejercicios con herencia, encapsulamiento y polimorfismo.

| Número | Descripción | Estado |
|---------|-------------|--------|
| 1  | Crear una clase `Animal` con un método `hacer_sonido()`. |  |
| 2  | Crear subclases `Perro` y `Gato` que hereden de `Animal`. |  |
| 3  | Sobreescribir `hacer_sonido()` en `Perro` y `Gato`. |  |
| 4  | Definir una clase `Empleado` con un método `calcular_salario()`. |  |
| 5  | Crear subclases `Gerente` y `Programador` con salario diferente. |  |
| 6  | Implementar `@property` y `@setter` en `CuentaBancaria`. |  |
| 7  | Crear una clase `Figura` con un método `area()`. |  |
| 8  | Crear subclases `Circulo` y `Rectangulo`. |  |
| 9  | Implementar `__str__` en `Persona` para representación en texto. |  |
| 10 | Crear una clase `Biblioteca` con una lista de libros. |  |
| 11 | Implementar `agregar_libro()` y `eliminar_libro()`. |  |
| 12 | Crear una clase `Pedido` con estado (`pendiente`, `entregado`). |  |
| 13 | Implementar `marcar_como_entregado()`. |  |
| 14 | Crear una clase `Restaurante` con una lista de `Pedidos`. |  |
| 15 | Implementar `mostrar_pedidos_pendientes()`. |  |


 > ## Nivel Avanzado
> - Ejercicios con patrones de diseño y conceptos avanzados de POO.

| Número | Descripción | Estado |
|---------|-------------|--------|
| 1  | Implementar un Singleton en Python. |  |
| 2  | Crear una clase `Logger` que siga el patrón Singleton. |  |
| 3  | Implementar el patrón `Factory Method`. |  |
| 4  | Crear un sistema de gestión de usuarios con `Observer`. |  |
| 5  | Implementar `__iter__` y `__next__` en una clase personalizada. |  |
| 6  | Crear una clase `Producto` con `@classmethod`. |  |
| 7  | Usar `@staticmethod` para una función de utilidad. |  |
| 8  | Implementar una jerarquía con `ABC` y `@abstractmethod`. |  |
| 9  | Crear una clase `Vehiculo` con `métodos abstractos`. |  |
| 10 | Crear una clase `Juego` con `estado` y `patrón Estado`. |  |
| 11 | Implementar `decoradores` en una clase. |  |
| 12 | Crear una API con `Flask` y una clase `Usuario`. |  |
| 13 | Implementar un `Gestor de Configuración` con JSON. |  |
| 14 | Crear una `Cola` usando `deque` y `clases`. |  |
| 15 | Implementar `multiprocesamiento` con POO. |  |

- ## Ejercicio Bonus: Desafío de Lógica
**Problema:** _Hay tres interruptores en una habitación. Solo uno de ellos enciende una bombilla en una habitación contigua. Puedes entrar a la habitación de la bombilla una sola vez. ¿Cómo averiguar cuál interruptor la enciende?_
