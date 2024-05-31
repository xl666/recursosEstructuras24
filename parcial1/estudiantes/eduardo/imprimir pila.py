class Pila():
    def __init__(self):
        self.interna = []

    def push(self, valor):
        for _ in valor:
            self.interna.append(_)

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

def imprimir_pila_en_orden(pila):
    elementos = []
    while pila.interna:
        elementos.append(pila.pop())
    elementos.sort()  
    print(','.join(map(str, elementos)))

n = int(input().strip())
valores = input().strip().split(',')

pila = Pila()
pila.push(valores)

imprimir_pila_en_orden(pila)