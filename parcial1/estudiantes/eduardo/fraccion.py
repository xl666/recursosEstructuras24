class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __eq__(self, otra_fraccion):
        return self.numerador * otra_fraccion.denominador == otra_fraccion.numerador * self.denominador

def leer_numeros():
    numerador1 = int(input())
    denominador1 = int(input())
    numerador2 = int(input())
    denominador2 = int(input())
    return numerador1, denominador1, numerador2, denominador2

def main():
    numerador1, denominador1, numerador2, denominador2 = leer_numeros()
    
    fraccion1 = Fraccion(numerador1, denominador1)
    fraccion2 = Fraccion(numerador2, denominador2)
    
    print(fraccion1 == fraccion2)

if __name__ == "__main__":
    main()