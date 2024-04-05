import math

class Circulo:
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def mostrar_informacion(self):
        print("Radio:", self.radio)
        print("Color:", self.color)
        print("Área:", self.calcular_area())

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))
    color = input("Ingrese el color del círculo: ")
    circulo = Circulo(radio, color)
    circulo.mostrar_informacion()
