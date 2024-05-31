#En matemáticas se dice que una expresión está balanceada si los paréntesis de agrupamiento se utilizaron correctamente.
P#or ejemplo, la expresión:
#(4+4*(9+3) + (5/6))

#Está balanceada, para cada paréntesis que abre, hay uno que cierra y no se trata de cerrar uno sin que haya 
#otro abierto correspondiente

#Por ejemplo, la expresión:

#5+6( 5-2))(

#No está balanceada ya que tiene un paréntesis que cierra extra y el último paréntesis que abre
#no tiene uno correspondiente que cierra.

#Crea una función que reciba una cadena similar a la de los ejemplos, la función regresa verdadero 
#si la expresión está balanceada y falso de lo contrario.

#Debes utilizar una pila para resolver el problema, toma el código del recurso (implementación vista en clase)
#Ejemplo de entrada
#(1+1*(2/5 +(7-2)))
#Ejemplo de salida
#True
class Pila():
    def __init__(self):
        self.interna = []

    def esta_vacia(self):
        return len(self.interna) == 0
        
    def push(self, valor):
        self.interna.append(valor)

    def pop(self):
        if not self.interna:
            return None
        return self.interna.pop()

    def peek(self):
        if not self.interna:
            return None
        return self.interna[-1]

    def __repr__(self):
        return str(self.interna)


def esta_balanceada(expresion):
    pila = Pila()
    for c in expresion:
        if c == '(':
            pila.push(0)
        if c == ')':
            if pila.esta_vacia():
                return False
            pila.pop()
    if not pila.esta_vacia():
        return False
    return True
    
if __name__ == '__main__':
    cadena = input()
    print(esta_balanceada(cadena))