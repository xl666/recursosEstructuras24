class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Velocidad:", self.velocidad)

if __name__ == "__main__":
    marca = input("Ingrese la marca del coche: ")
    modelo = input("Ingrese el modelo del coche: ")
    color = input("Ingrese el color del coche: ")
    coche = Coche(marca, modelo, color)
    coche.mostrar_informacion()
    coche.acelerar(50)
    coche.mostrar_informacion()
