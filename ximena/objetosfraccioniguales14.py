# Considerando el código visto en clase sobre fracciones (el cual se adjunta en este ejercicio)
#agrega la implementación del método __eq__ de tal forma que sea posible establecer
#si dos fracciones son iguales mediante una comparación.

#El programa recibe 4 números en el siguiente orden: 
#- numerador fracción 1
#- denominador fracción 1
#- numerador fracción 2
#- denominador fracción 2

#Se debe imprimir True si ambas fracciones son iguales desde un punto de vista matemático
#De no ser iguales se imprime False

#El ejercicio se debe resolver con clases y objetos, se revisarán los códigos
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
        return (self.numerador * otra.denominador) == (otra.numerador * self.denominador)
    
if __name__ == '__main__':
    n1 = int(input())
    d1 = int(input())
    n2 = int(input())
    d2 = int(input())

    f1 = Fraccion(n1, d1)
    f2 = Fraccion(n2, d2)
    print(f1 == f2)
