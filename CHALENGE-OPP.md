# Ejercicios de Programación Orientada a Objetos (POO) en Python

Este repositorio contiene una lista de ejercicios para practicar y dominar los conceptos de Programación Orientada a Objetos (POO) en Python. Los ejercicios están organizados en tres niveles de dificultad: Principiante, Intermedio y Avanzado, con 15 ejercicios en cada nivel. Además, se incluye un ejercicio Bonus al final, que es un desafío de lógica común en entrevistas de trabajo.

> - _Puedes resolver estos ejercicios en Python o en cualquier otro lenguaje de programación que prefieras. ¡El objetivo es aprender y practicar!_


    - Ejercicios para familiarizarse con los conceptos básicos de POO en Python.


| #  | Clase/Componente     | Métodos/Acciones                  | Dificultad | Relaciones      |
|----|----------------------|-----------------------------------|------------|-----------------|
| 1  | Persona              | `saludar`, `es_mayor`             | ⭐         | -               |
| 2  | Estudiante           | `estudiar`, `saludar`•            | ⭐         | Hereda Persona  |
| 3  | Animal               | `hacer_sonido`                    | ⭐         | -               |
| 4  | Perro                | `hacer_sonido`•, `mover_cola`     | ⭐         | Hereda Animal   |
| 5  | Rectángulo           | `area`, `perimetro`               | ⭐         | -               |
| 6  | Círculo              | `area`•, `perimetro`•             | ⭐⭐       | -               |
| 7  | Producto             | `aplicar_descuento`               | ⭐         | -               |
| 8  | Carrito              | `agregar_producto`, `total`       | ⭐⭐       | Usa Producto    |
| 9  | Usuario              | `login`, `logout`                 | ⭐         | -               |
| 10 | Admin                | `banear_usuario`•                 | ⭐⭐       | Hereda Usuario  |
| 11 | Reloj                | `mostrar_hora`, `ajustar`         | ⭐         | -               |
| 12 | Contacto             | `mostrar_info`                    | ⭐         | -               |
| 13 | Agenda               | `agregar_contacto`, `buscar`      | ⭐⭐       | Usa Contacto    |
| 14 | Coche                | `acelerar`, `frenar`              | ⭐⭐       | -               |
| 15 | Moto                 | `hacer_caballito`•                | ⭐⭐       | Hereda Coche    |
| 16 | Libro                | `abrir`, `cerrar`                 | ⭐         | -               |
| 17 | Biblioteca           | `prestar_libro`, `devolver`       | ⭐⭐       | Usa Libro       |
| 18 | Tarea                | `completar`, `mostrar`            | ⭐         | -               |
| 19 | ListaTareas          | `agregar`, `eliminar`             | ⭐⭐       | Usa Tarea       |
| 20 | CuentaBancaria       | `depositar`, `retirar`            | ⭐⭐       | -               |

> - Ejercicios con herencia, encapsulamiento y polimorfismo.

| #  | Clase/Componente     | Métodos/Acciones                  | Dificultad | Relaciones               |
|----|----------------------|-----------------------------------|------------|--------------------------|
| 1  | Empleado             | `calcular_salario`                | ⭐⭐⭐     | -                        |
| 2  | Gerente              | `calcular_salario`•               | ⭐⭐⭐     | Hereda Empleado          |
| 3  | Figura (abstracta)   | `area`, `perimetro`               | ⭐⭐⭐     | ABC                      |
| 4  | Triángulo            | `area`•, `perimetro`•             | ⭐⭐⭐     | Hereda Figura            |
| 5  | SistemaPago          | `procesar_pago`                   | ⭐⭐⭐     | Strategy                 |
| 6  | Notificador          | `enviar`                          | ⭐⭐⭐     | Observer                 |
| 7  | Pedido               | `agregar_item`, `calcular`        | ⭐⭐⭐     | Usa Producto             |
| 8  | Restaurante          | `tomar_pedido`, `servir`          | ⭐⭐⭐     | Usa Pedido               |
| 9  | Juego                | `iniciar`, `actualizar`           | ⭐⭐⭐     | State                    |
| 10 | Personaje            | `mover`, `atacar`                 | ⭐⭐⭐     | Component                |
| 11 | Arma                 | `disparar`, `recargar`            | ⭐⭐⭐     | Usa Personaje            |
| 12 | Enemigo              | `recibir_daño`•                   | ⭐⭐⭐     | Hereda Personaje         |
| 13 | Inventario           | `agregar`, `usar`                 | ⭐⭐⭐     | Composite                |
| 14 | Chat                 | `enviar_mensaje`, `buscar`        | ⭐⭐⭐     | Singleton                |
| 15 | ConexiónDB           | `conectar`, `query`               | ⭐⭐⭐     | Factory                  |
| 16 | Logger               | `log`, `guardar`                  | ⭐⭐⭐     | Decorator                |
| 17 | Validación           | `validar_email`, `validar_DNI`    | ⭐⭐⭐     | Static                   |
| 18 | API                  | `get`, `post`                     | ⭐⭐⭐⭐   | Adapter                  |
| 19 | Traductor            | `traducir`                        | ⭐⭐⭐⭐   | Proxy                    |
| 20 | SistemaArchivos      | `crear`, `eliminar`               | ⭐⭐⭐⭐   | Facade                   |


> - Ejercicios con patrones de diseño y conceptos avanzados de POO.

| #  | Clase/Componente     | Métodos/Acciones                  | Dificultad | Patrón/Concepto          |
|----|----------------------|-----------------------------------|------------|--------------------------|
| 1  | MetaClase            | `__new__`, `__prepare__`          | ⭐⭐⭐⭐⭐ | Metaclases               |
| 2  | ThreadPool           | `submit`, `map`                   | ⭐⭐⭐⭐⭐ | Concurrencia             |
| 3  | ServidorAsync        | `start`, `handle_request`         | ⭐⭐⭐⭐⭐ | Async/Await              |
| 4  | ORM                  | `save`, `query`                   | ⭐⭐⭐⭐⭐ | SQLAlchemy-like          |
| 5  | WebScraper           | `scrape`, `parse`                 | ⭐⭐⭐⭐⭐ | Multihilo                |
| 6  | JITCompiler          | `compile`, `optimize`             | ⭐⭐⭐⭐⭐ | Decoradores avanzados    |
| 7  | Blockchain           | `add_block`, `validate`           | ⭐⭐⭐⭐⭐ | Encadenamiento           |
| 8  | NeuralNetwork        | `train`, `predict`                | ⭐⭐⭐⭐⭐ | POO + ML                 |
| 9  | Microservicio        | `deploy`, `scale`                 | ⭐⭐⭐⭐⭐ | Arquitectura             |
| 10 | GraphQL              | `resolve`, `execute`              | ⭐⭐⭐⭐⭐ | Patrón Resolver          |
| 11 | CacheManager         | `get`, `set`, `invalidate`        | ⭐⭐⭐⭐⭐ | Flyweight                |
| 12 | DSL                  | `parse`, `evaluate`               | ⭐⭐⭐⭐⭐ | Lenguaje específico      |
| 13 | LoadBalancer         | `add_server`, `route_request`     | ⭐⭐⭐⭐⭐ | Round-Robin              |
| 14 | PubSub               | `subscribe`, `publish`            | ⭐⭐⭐⭐⭐ | Mensajería               |
| 15 | CircuitBreaker       | `call`, `reset`                   | ⭐⭐⭐⭐⭐ | Tolerancia fallos        |
| 16 | DataPipeline         | `extract`, `transform`, `load`    | ⭐⭐⭐⭐⭐ | ETL                      |
| 17 | RecommendationEngine | `train_model`, `get_recommendations` | ⭐⭐⭐⭐⭐ | Machine Learning        |
| 18 | EncryptionService    | `encrypt`, `decrypt`              | ⭐⭐⭐⭐⭐ | Seguridad                |
| 19 | QuantumSimulator     | `run_circuit`                     | ⭐⭐⭐⭐⭐ | (Bonus teórico)          |
| 20 | AIAgent              | `perceive`, `act`, `learn`        | ⭐⭐⭐⭐⭐ | IA                       |

## 🧩 Desafío de Lógica POO

**Problema:** Hay tres interruptores en una habitación. Solo uno enciende una bombilla en otra habitación. Puedes entrar una sola vez. 

```python
class AcertijoInterruptores:
    def __init__(self):
        # Estados iniciales de los 3 interruptores
        self.interruptores = {
            1: False,
            2: False, 
            3: False
        }
        self.bombilla = Bombilla()
    
    def resolver_acertijo(self):
        """
        ¡Completa este método para resolver el acertijo!
        Debes manipular los interruptores estratégicamente
        y verificar el estado de la bombilla para determinar
        cuál interruptor la controla.
        
        Pistas:
        1. Puedes usar time.sleep() para simular esperas
        2. La bombilla tiene propiedades observables
        3. Solo un interruptor es el correcto
        """
        # ¡Tu implementación va aquí!
        pass

class Bombilla:
    def __init__(self):
        self.encendida = False
        self.temperatura = 25  # Temperatura ambiente en °C
    
    def actualizar_estado(self, interruptor_activo):
        """
        Actualiza el estado físico de la bombilla
        según el interruptor que esté activo actualmente.
        """
        # ¡Completa esta lógica!
        pass
    
    def obtener_estado(self):
        """
        Devuelve un dict con el estado observable:
        - encendida: bool
        - temperatura: int
        - descripcion: str
        """
        # ¡Implementa esta observación clave!
        return {
            "encendida": False,
            "temperatura": 25,
            "descripcion": "Implementar según estado real"
        }```
    
