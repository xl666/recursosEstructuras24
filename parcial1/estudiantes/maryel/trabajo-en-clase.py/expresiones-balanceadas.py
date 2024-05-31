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

    def __repr__(self):
        return str(self.interna)


def expresiones_balanceada(expresion):
    pila = Pila()
    for char in expresion:
        if char == '(':
            pila.push(char)
        elif char == ')':
            if pila.peek() is None:
                return False
            pila.pop()
    return pila.peek() is None


expresion = input().strip()

print(expresiones_balanceada(expresion))
