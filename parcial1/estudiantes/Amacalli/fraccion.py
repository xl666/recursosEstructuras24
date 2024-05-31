class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    # función que se invoca al hacer print del objeto
    def __repr__(self):
        return '%s/%s' % (self.numerador, self.denominador)

    def __eq__(self, otra):
        if not isinstance(otra, Fraccion):
            return False
        else:
            pass

if __name__ == '__main__':
    n1 = int(input())
    d1 = int(input())
    n2 = int(input())
    d2 = int(input())

    print()