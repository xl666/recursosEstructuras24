class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def tamano(self):
        return len(self.items)


def expresion_balanceada(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.esta_vacia():
                return False
            else:
                pila.pop()
    return pila.esta_vacia()



expresion = input()


balanceado = expresion_balanceada(expresion)
print(balanceado)