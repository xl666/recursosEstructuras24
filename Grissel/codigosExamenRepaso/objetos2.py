# - - - Método para calcular el área de un rectángulo en una clase Rectangulo
class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def calcular_area(self): # este es un método
        return self.ancho * self.altura

# Crear objeto de la clase Rectangulo
rectangulo = Rectangulo(5, 10)

# Llamar al método para calcular el área del rectángulo
area = rectangulo.calcular_area()
print("Área del rectángulo:", area)

# - - - Método para saludar en una clase Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self): # este es un método
        print(f"Hola, soy {self.nombre}. ¡Mucho gusto!")

# Crear objeto de la clase Persona
persona = Persona("Juan")

# Llamar al método para que la persona salude
persona.saludar()

# - - - Método para verificar si un número es par en una clase Numero
class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def es_par(self): # este es un método
        if self.valor % 2 == 0:
            return True
        else:
            return False

# Crear objeto de la clase Numero
numero = Numero(7)

# Llamar al método para verificar si el número es par
if numero.es_par():
    print("El número es par.")
else:
    print("El número es impar.")