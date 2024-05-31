class Nodo():
    def __init__(self, indice, padre = None):
        self.hijos = []
        self.indice = indice
        self.padre = padre

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
        nuevo = Nodo(indice,indicePadre)
        if not self.raiz:
            self.raiz = nuevo
            return True 
        padre = self.regresarNodo(indicePadre)
        nuevo = Nodo(indice, padre)
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
        nodo = self.regresarNodo(indice) # buscar nodo y si no hay regresar False
        if nodo is None: # if not nodo:
            return False
        return len(nodo.hijos) == 0 # si nodo  si está y no tiene hijos (que sea igual a 0), entonces es una hoja
    
    def es_padre(self, indice: int) -> int:
        """
        Determina si un nodo en un índice dado es padre.

        self, indice: int
        returns: int
        """
        nodo_interes = self.regresarNodo_rec(indice)
        if not nodo_interes:
            return None
        return nodo_interes.padre.indice

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
    print(arbol.es_padre(indice))