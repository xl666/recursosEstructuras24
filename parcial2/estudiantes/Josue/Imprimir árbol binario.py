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

def leer_arbol(nodos: int) -> ArbolBinarioBusqueda:
    arbol = ArbolBinarioBusqueda()
    for _ in range(nodos):
        entrada = input().split(':')
        indice = int(entrada[0])
        valor = entrada[1]
        arbol.agregar_nodo(indice, valor)
    return arbol

if __name__ == '__main__':
    nodos = int(input())
    arbol = leer_arbol(nodos)
    print(arbol)
