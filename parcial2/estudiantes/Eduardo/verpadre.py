class Nodo():
    def __init__(self, indice, padre=None):
        self.hijos = []
        self.indice = indice
        self.padre = padre

    def agregar_hijo(self, hijo):
        hijo.padre = self
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
    
    def obtener_padre(self, indice):
        nodo = self.regresarNodo(indice)
        if nodo is None or nodo.padre is None:
            return None
        return nodo.padre.indice

    def es_hoja(self, indice: int) -> bool:
        """
        Determina si un nodo en un índice dado es una hoja.

        self, indice: int
        returns: bool
        """
        nodo = self.regresarNodo(indice) #agarra lo que este dentro del indice y lo almacena en nodo
        if nodo is None: #si el nodo no esta en el arbol se devuelve false, pues no existe
            return False
        return not nodo.hijos #si si esta, se revisa con "not" si la lista de hijos del nodo esta vacia, si esta vacia, esntonces es hoja y devuelve true

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
    

if __name__ == '__main__':
    indice = int(input())
    nodos = int(input())
    arbol = leer_arbol(nodos)   
    print(arbol.obtener_padre(indice))