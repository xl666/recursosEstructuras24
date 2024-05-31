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
    
def imprimir_pila(pila):
    if not pila.peek():
        return
    primero = pila.pop()
    print(primero, end='')
    while pila.peek():
        print(',' + str(pila.pop()), end='')
    print('')

def imprimir_pila2(pila):
    lista = []
    while pila.peek():
        lista.append(str(pila.pop()))
    print(','.join(lista))

def esta_balanceada(expresion):
    pila = Pila()
    for c in expresion:
        if c == '(':
            pila.push(0)
        if c == ')':
            if pila.esta_vacia():
                print()
                return False
            pila.pop()
    if not pila.esta_vacia():
        return False
    return True



if __name__ == '__main__':
    cadena = input()
    print(esta_balanceada(cadena))
