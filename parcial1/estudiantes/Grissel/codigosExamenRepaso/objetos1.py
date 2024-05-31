# - - - Clase Persona para representar a una persona con nombre y edad
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear objetos de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Utilizar métodos de la clase Persona
print(persona1.presentarse()) # ¡Hola! Mi nombre es Juan y tengo 30 años.
print(persona2.presentarse()) # ¡Hola! Mi nombre es María y tengo 25 años.

# - - - Clase Rectangulo para representar un rectángulo con ancho y altura
class Rectangulo():
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def calcular_area(self):
        return self.ancho * self.altura

# Crear objetos de la clase Rectangulo
rectangulo1 = Rectangulo(5, 10)
rectangulo2 = Rectangulo(3, 7)

# Utilizar métodos de la clase Rectangulo
print("Área del rectángulo 1:", rectangulo1.calcular_area()) # Área del rectángulo 1: 50
print("Área del rectángulo 2:", rectangulo2.calcular_area()) # Área del rectángulo 2: 21

# - - - Clase Libro para representar un libro con título y autor
class Libro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def informacion(self):
        return f"El libro '{self.titulo}' fue escrito por {self.autor}."

# Crear objetos de la clase Libro
libro1 = Libro("Harry Potter", "J.K. Rowling")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")

# Utilizar métodos de la clase Libro
print(libro1.informacion()) # El libro 'Harry Potter' fue escrito por J.K. Rowling.
print(libro2.informacion()) # El libro 'Cien años de soledad' fue escrito por Gabriel García Márquez.