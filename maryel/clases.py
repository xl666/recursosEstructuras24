class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

pepe = Persona('Pepe', 20)
print(pepe.edad)
juan = Persona('Juan', 15)
print(juan.nombre)