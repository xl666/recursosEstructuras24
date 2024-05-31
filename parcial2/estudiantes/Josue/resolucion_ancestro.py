class Nodo():
    def __init__(self, indice):
        self.hijos = []
        self.indice = indice

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __repr__(self):
        return 'n:%s' % self.indice

class Arbol():
    """
    Implementación de un árbol general
    que guarda índices
    los índices son únicos
    """
    def __init__(self):
        self.raiz = None

    def regresarNodo_rec(self, indice, actual, resultado):
        """
        Regresa el objeto nodo con el
        índice dado
        """
        if actual.indice == indice:        
            resultado.append(actual)
            return # un poco de poda aunque sea
        
        for hijo in actual.hijos:
            self.regresarNodo_rec(indice, hijo, resultado)

    def regresarNodo(self, indice):
        res = []
        self.regresarNodo_rec(indice, self.raiz, res)
        if not res:
            return None
        return res[0]

    def agregar_hijo(self, indice, indicePadre=None):
        nuevo = Nodo(indice)
        if not self.raiz:
            self.raiz = nuevo
            return True 
        padre = self.regresarNodo(indicePadre)
        if not padre:
            return False
        padre.agregar_hijo(nuevo)
        return True

    def es_hoja(self, indice: int) -> bool:
        """
        Determina si un nodo en un índice dado es una hoja.

        self, indice: int
        returns: bool
        """
        nodo = self.regresarNodo(indice)
        if not nodo:
            return False
        return not nodo.hijos


    def imprimir_arbol(self):
        """
        Imprime el árbol de manera recursiva.
        """
        def imprimir_rec(nodo, nivel):
            print('|' * nivel + ' ' + str(nodo.indice))
            for hijo in nodo.hijos:
                imprimir_rec(hijo, nivel + 1)
        
        if self.raiz:
            imprimir_rec(self.raiz, 0)
    
    

def leer_arbol(nodos: int) -> Arbol:
    """
    Para leer árboles que pasa el sistema.
    Regresa el árbol resultante

    nodos: int
    returns: Arbol
    """
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


def es_ancestro(arbol: ) -> bool:
    nodoB = arbol.regresarNodo(indideB)
    if nor nodoB:
        return False
    actual = nodoB
    siguiente = nodoB.padre
    while siguiente != None:
        if siguiente.indice == indiceA:
            return True
        siguiente = siguiente.padre
    return False



if __name__ == '__main__':
    indiceA = int(input())
    indiceB = int(input())
    nodos = int(input())
    arbol = leer_arbol(nodos)
    print(arbol.es_ancestro(indiceA, indiceB))