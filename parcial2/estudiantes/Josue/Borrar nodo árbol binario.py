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

    def borrar_nodo(self, indice):
        self.raiz = self._borrar_nodo_rec(self.raiz, indice)

    def _borrar_nodo_rec(self, actual, indice):
        if actual is None:
            return actual
        if indice < actual.indice:
            actual.izquierda = self._borrar_nodo_rec(actual.izquierda, indice)
        elif indice > actual.indice:
            actual.derecha = self._borrar_nodo_rec(actual.derecha, indice)
        else:
            if actual.izquierda is None:
                return actual.derecha
            elif actual.derecha is None:
                return actual.izquierda
            sucesor = self._min_value_node(actual.derecha)
            actual.indice = sucesor.indice
            actual.valor = sucesor.valor
            actual.derecha = self._borrar_nodo_rec(actual.derecha, sucesor.indice)
        return actual

    def _min_value_node(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def convertir_a_cadena_arbol_rec(self, nodo, nivel, res):
        if nodo is None:
            return
        espacios = '| ' * nivel
        res.append(f"{espacios}{nodo.indice}:{nodo.valor}")
        if nodo.izquierda:
            self.convertir_a_cadena_arbol_rec(nodo.izquierda, nivel + 1, res)
        if nodo.derecha:
            self.convertir_a_cadena_arbol_rec(nodo.derecha, nivel + 1, res)

    def __repr__(self):
        if self.raiz is None:
            return ''
        res = []
        self.convertir_a_cadena_arbol_rec(self.raiz, 0, res)
        return '\n'.join(res)

def leer_arbol_y_borrar(nodos: int, indice_borrar: int) -> ArbolBinarioBusqueda:
    arbol = ArbolBinarioBusqueda()
    for _ in range(nodos):
        entrada = input().split(':')
        indice = int(entrada[0])
        valor = entrada[1]
        arbol.agregar_nodo(indice, valor)
    arbol.borrar_nodo(indice_borrar)
    return arbol

if __name__ == '__main__':
    indice_borrar = int(input())
    nodos = int(input())
    arbol = leer_arbol_y_borrar(nodos, indice_borrar)
    print(arbol)
