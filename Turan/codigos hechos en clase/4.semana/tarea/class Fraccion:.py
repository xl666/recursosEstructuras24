class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        mcd = self.calcular_mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def calcular_mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __eq__(self, otra_fraccion):
        # Simplificar ambas fracciones antes de compararlas
        self.simplificar()
        otra_fraccion.simplificar()

        return self.numerador == otra_fraccion.numerador and self.denominador == otra_fraccion.denominador

if __name__ == '__main__':
    # Leer los cuatro números enteros
    numerador1 = int(input())
    denominador1 = int(input())
    numerador2 = int(input())
    denominador2 = int(input())
    fraccion1 = Fraccion(numerador1, denominador1)
    fraccion2 = Fraccion(numerador2, denominador2)

   
    print(fraccion1 == fraccion2)
