class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente_nodo = None

class Lista:
    def __init__(self, valor):
        self.cabeza = Nodo(valor)

    def append(self, valor):
        nuevo_nodo = Nodo(valor)
        actual = self.cabeza
        while actual.siguiente_nodo is not None:
            actual = actual.siguiente_nodo
        actual.siguiente_nodo = nuevo_nodo

    def get(self, pos):
        if pos < 0:
            return None
        actual = self.cabeza
        for _ in range(pos):
            if actual is None:
                return None
            actual = actual.siguiente_nodo
        if actual is None:
            return None
        return actual.valor

posicion = int(input())
cantidad_valores = int(input())
valores = [int(input()) for _ in range(cantidad_valores)]

lista = Lista(valores[0])
for valor in valores[1:]:
    lista.append(valor)

resultado = lista.get(posicion)
print(resultado)