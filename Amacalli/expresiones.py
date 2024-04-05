class Pila():
    def __init__(self):
        self.interna = []

    def esta_vacia(self):
        return len(self.interna()) == 0
    
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

def esta_balanceada (expresion):
    pila = Pila()
    for c in expresion:
        if c == '(':
            pila.push(1)
        if c == ')':
            if pila.esta_vacia():
                return False
            pila.pop()
    if pila.peek():
        return False
    return True

if __name__ == '__main__':
     cadena = input()
     print(esta_balanceada(cadena))