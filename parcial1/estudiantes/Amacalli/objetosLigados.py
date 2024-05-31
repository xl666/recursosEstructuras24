class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Lista:
    def __init__(self, valor=None):
        if valor is not None:
            self.cabeza = Nodo(valor)
        else:
            self.cabeza = None

    def append(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def get(self, pos):
        actual = self.cabeza
        index = 0
        while actual is not None:
            if index == pos:
                return actual.valor
            actual = actual.siguiente
            index += 1
        return None


p = int(input())
n = int(input())


if n > 0:
    valor_inicial = int(input())
    l = Lista(valor_inicial)
    for _ in range(n - 1):
        valor = int(input())
        l.append(valor)
else:
    l = Lista()

print(l.get(p))

