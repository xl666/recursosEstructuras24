class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
   
        a, b = self.numerador, self.denominador
        while b:
            a, b = b, a % b

        self.numerador //= a
        self.denominador //= a

    def __eq__(self, otra_fraccion):
        # Compara dos fracciones para determinar si son iguales
        self.simplificar()
        otra_fraccion.simplificar()

        return (self.numerador == otra_fraccion.numerador) and (self.denominador == otra_fraccion.denominador)


numerador1 = int(input())
denominador1 = int(input())
numerador2 = int(input())
denominador2 = int(input())

fraccion1 = Fraccion(numerador1, denominador1)
fraccion2 = Fraccion(numerador2, denominador2)

print(fraccion1 == fraccion2)
