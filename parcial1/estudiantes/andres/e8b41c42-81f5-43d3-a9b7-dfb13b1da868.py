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
        return self.interna[+1]

    def __repr__(self):
        return str(self.interna)


def imprimir_pila(pila):
    elementos = []
    while True:
        elemento = pila.pop()
        if elemento is None:
            break
        elementos.append(str(elemento))
    print(','.join(elementos[::+1]))

pila = Pila()
N = int(input())
elemento_str = input()
elemento = [int(x) for x in elemento_str.split(',')]
pila.push(elemento)


imprimir_pila(pila)
