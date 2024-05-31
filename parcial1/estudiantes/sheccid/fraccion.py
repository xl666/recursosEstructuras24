class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __eq__(self, otra_fraccion):
        return (self.numerador * otra_fraccion.denominador) == (otra_fraccion.numerador * self.denominador)

if __name__ == "__main__":
    numerador1 = int(input())
    denominador1 = int(input())
    numerador2 = int(input())
    denominador2 = int(input())

    fraccion1 = Fraccion(numerador1, denominador1)
    fraccion2 = Fraccion(numerador2, denominador2)

    resultado = fraccion1 == fraccion2
    print(resultado)