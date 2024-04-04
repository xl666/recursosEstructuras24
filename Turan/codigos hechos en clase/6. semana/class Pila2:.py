class Pila:
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

def balanceada(cadena):
    pila = Pila()
    for element in cadena:
        if element == '(':
            pila.push(element)
        elif element == ')':
            if pila.peek() == '(':
                pila.pop()
            else:
                return False
    return pila.peek() is None

if __name__ == '__main__':
    cadena = input().strip()
    print(balanceada(cadena))
