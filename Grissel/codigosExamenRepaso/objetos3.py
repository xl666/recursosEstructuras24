# - - - Comparación de atributos en una clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __eq__(self, other):
        return self.nombre == other.nombre and self.edad == other.edad

# Crear objetos de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("Juan", 30)
persona3 = Persona("María", 25)

# Comparar objetos de la clase Persona
print("¿persona1 es igual a persona2?", persona1 == persona2)
print("¿persona1 es igual a persona3?", persona1 == persona3)

# insistance
# - - - ejemplo que utiliza la función isinstance() para determinar si un objeto es una instancia de una clase específica
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def ladrar(self):
        print("¡Guau!")

class Gato(Animal):
    def maullar(self):
        print("¡Miau!")

# Crear instancias de las clases
mi_perro = Perro("Buddy")
mi_gato = Gato("Whiskers")

# Verificar si las instancias pertenecen a la clase Animal
print("¿mi_perro es una instancia de Animal?", isinstance(mi_perro, Animal))
print("¿mi_gato es una instancia de Animal?", isinstance(mi_gato, Animal))

# Verificar si las instancias pertenecen a las clases Perro y Gato
print("¿mi_perro es una instancia de Perro?", isinstance(mi_perro, Perro))
print("¿mi_gato es una instancia de Gato?", isinstance(mi_gato, Gato))