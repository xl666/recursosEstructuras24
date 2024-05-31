class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Lista():
    def __init__(self):
        self.cabeza = None

    def append(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def get(self, pos):
        if pos < 0:  
            return None
        actual = self.cabeza
        indice = 0
        while actual is not None:
            if indice == pos:
                return actual.valor
            actual = actual.siguiente
            indice += 1
        return None

if __name__ == '__main__':
    p = int(input())
    n = int(input())
    lista = Lista()
    for i in range(n):
        lista.append(int(input()))
        
    resultado = lista.get(p)
    print(resultado)
