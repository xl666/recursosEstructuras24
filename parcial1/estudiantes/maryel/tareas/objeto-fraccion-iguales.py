class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __repr__(self):
        return '%s/%s' % (self.numerador, self.denominador)

    def __eq__(self, otra_fracc):
        return self.numerador * otra_fracc.denominador == otra_fracc.numerador * self.denominador


num1 = int(input())
denom1 = int(input())
num2 = int(input())
denom2 = int(input())

fraccion1 = Fraccion(num1, denom1)
fraccion2 = Fraccion(num2, denom2)

print(fraccion1 == fraccion2)
