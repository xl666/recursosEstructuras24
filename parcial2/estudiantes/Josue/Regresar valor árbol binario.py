class Nodo:
    def __init__(self, indice, valor):
        self.indice = indice
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, indice, valor):
        if self.raiz is None:
            self.raiz = Nodo(indice, valor)
        else:
            self._agregar_nodo_rec(self.raiz, indice, valor)

    def _agregar_nodo_rec(self, actual, indice, valor):
        if indice < actual.indice:
            if actual.izquierda is None:
                actual.izquierda = Nodo(indice, valor)
            else:
                self._agregar_nodo_rec(actual.izquierda, indice, valor)
        else:
            if actual.derecha is None:
                actual.derecha = Nodo(indice, valor)
            else:
                self._agregar_nodo_rec(actual.derecha, indice, valor)

    def regresar_valor(self, indice):
        actual = self.raiz
        while actual is not None:
            if actual.indice == indice:
                return actual.valor
            elif indice < actual.indice:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return None

def leer_arbol(nodos: int) -> ArbolBinarioBusqueda:
    arbol = ArbolBinarioBusqueda()
    for _ in range(nodos):
        entrada = input().split(':')
        indice = int(entrada[0])
        valor = entrada[1]
        arbol.agregar_nodo(indice, valor)
    return arbol

if __name__ == '__main__':
    indice = int(input())
    nodos = int(input())
    arbol = leer_arbol(nodos)
    print(arbol.regresar_valor(indice))

