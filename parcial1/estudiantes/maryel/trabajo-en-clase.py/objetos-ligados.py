class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Lista:
    def __init__(self, valor):
        self.cabeza = Nodo(valor)

    def append(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    def get(self, pos):
        if pos < 0:
            return None
        indice = 0
        actual = self.cabeza
        while actual:
            if indice == pos:
                return actual.valor
            actual = actual.siguiente
            indice += 1
        return None


if __name__ == '__main__':
    p = int(input())
    n = int(input())
    l = Lista(int(input()))
    for _ in range(n - 1):
        l.append(int(input()))

    print(l.get(p))
