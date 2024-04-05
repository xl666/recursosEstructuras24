class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Lista():
    def __init__(self, valor):
        self.cabeza = Nodo(valor)

    def append(self, valor):
        aux = self.cabeza
        while aux.siguiente is not None:
            aux = aux.siguiente
        aux.siguiente = Nodo(valor)

    def get(self, pos):
        aux = self.cabeza
        indice = 0
        while aux is not None:
            if indice == pos:
                return aux.valor
            aux = aux.siguiente
            indice += 1
        return None

if __name__ == '__main__':
    p = int(input())
    n = int(input())
    valores = [int(input())for _ in range(n)]
    l = Lista(valores[0])
    for valor in valores[1:]:
        l.append(valor)

print(l.get(p))
