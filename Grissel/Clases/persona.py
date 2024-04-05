class Persona:
    def __init__(self, nombre, edad, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Altura:", self.altura)
        print("Peso:", self.peso)
        print("IMC:", self.calcular_imc())

if __name__ == "__main__":
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    altura = float(input("Ingrese la altura de la persona (en metros): "))
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    persona = Persona(nombre, edad, altura, peso)
    persona.mostrar_informacion()
