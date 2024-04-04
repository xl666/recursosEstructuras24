
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

if __name__ == '__main__':
    n = int(input())
    pila = Pila()
    for _ in range(n):
        pila.push(int(input()))
    imprimir_pila(pila)
    
    
    
    
