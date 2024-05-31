class Fraccion:
    def __init__(self,numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador 
    
    def __eq__(self,other):
        return self.numerador * other.denominador == self.denominador * other.numerador
    
    def __repr__(self):
        return  self == other






if __name__ == '__main__':
    num1 = int(input())
    denom1 = int(input())
    num2 = int(input())
    denom2 = int(input())
    frac1 = Fraccion(num1,denom1)
    frac2 = Fraccion(num2,denom2)
    print(frac1 == frac2)