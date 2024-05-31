class Pila():
    def __init__(self):
        self.interna = []

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

    def esta_vacia(self):
        return len(self.interna) == 0

    def __repr__(self):
        return str(self.interna)

def expresion_balanceada(expresion):
    pila = Pila()

    for char in expresion:
        if char == '(':
            pila.push(char)
        elif char == ')':
            if pila.esta_vacia() or pila.pop() != '(':
                return False

    return pila.esta_vacia()


expresion = input()
print(expresion_balanceada(expresion))