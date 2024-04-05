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
    resultado = ""
    while True:
        valor = pila.pop()
        if valor is not None:
            resultado += str(valor) + ","
        else:
            break
    print(resultado[:-1])


n = int(input())
valores = input().split(',')

pila = Pila()
for valor in valores:
    pila.push(int(valor))

imprimir_pila(pila)
