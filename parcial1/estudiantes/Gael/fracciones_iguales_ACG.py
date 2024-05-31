class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    # función que se invoca al hacer print del objeto
    def __eq__(self,otro):
        return self.numerador/self.denominador==otro.numerador/otro.denominador
    
if __name__ == '__main__':
    numerador1=int(input())
    denominador1=int(input())
    numerador2=int(input())
    denominador2=int(input())
    fraccion1=Fraccion(numerador1,denominador1)
    fraccion2=Fraccion(numerador2,denominador2)
    print(fraccion1==fraccion2)
    