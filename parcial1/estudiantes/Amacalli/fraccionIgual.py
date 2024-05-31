class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __eq__(self, otra_fraccion):
        return self.numerador * otra_fraccion.denominador == self.denominador * otra_fraccion.numerador

# Entrada de datos
numerador1 = int(input())
denominador1 = int(input())
numerador2 = int(input())
denominador2 = int(input())

# Creación de objetos Fraccion
fraccion1 = Fraccion(numerador1, denominador1)
fraccion2 = Fraccion(numerador2, denominador2)

# Comparación de fracciones
print(fraccion1 == fraccion2)
