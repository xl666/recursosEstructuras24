class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) <= 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) <= 0:
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def balanceada(cadena):
    pila = Pila()
    for c in cadena:
        if c == '(':
            pila.push(c)
        elif c == ')':
            if pila.is_empty() or pila.peek() != '(':
                return False
            pila.pop()
    return pila.is_empty()