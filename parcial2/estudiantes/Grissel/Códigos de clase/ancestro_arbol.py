class Nodo():
    def __init__(self, indice, padre=None):
        self.hijos = []
        self.indice = indice
        self.padre = padre

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __repr__(self):
        return 'n:%s' % self.indice

class Arbol():
    def __init__(self):
        self.raiz = None

    def regresarNodo_rec(self, indice, actual, resultado):
        if actual.indice == indice:
            resultado.append(actual)
            return
        
        for hijo in actual.hijos:
            self.regresarNodo_rec(indice, hijo, resultado)

    def regresarNodo(self, indice):
        res = []
        self.regresarNodo_rec(indice, self.raiz, res)
        if not res:
            return None
        return res[0]

    def agregar_hijo(self, indice, indicePadre=None):
        if not self.raiz:
            nuevo = Nodo(indice)
            self.raiz = nuevo
            return True
        padre = self.regresarNodo(indicePadre)
        nuevo = Nodo(indice, padre)
        if not padre:
            return False
        padre.agregar_hijo(nuevo)
        return True

    def es_ancestro(self, ancestro, nodo):
        actual = self.regresarNodo(nodo)
        while actual is not None:
            if actual.indice == ancestro:
                return True
            actual = actual.padre
        return False

def leer_arbol(nodos):
    arbol = Arbol()
    if nodos == 0:
        return arbol
    
    indice_raiz = int(input())
    arbol.agregar_hijo(indice_raiz)
    for _ in range(nodos - 1):
        nodo, padre = input().split(':')
        nodo = int(nodo)
        padre = int(padre)
        arbol.agregar_hijo(nodo, padre)
    return arbol

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    n = int(input())
    arbol = leer_arbol(n)
    print(arbol.es_ancestro(a, b))
