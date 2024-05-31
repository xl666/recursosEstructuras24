
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
        if nodo is None:
            return False
        return not nodo.hijos
    def nodos_en_nivel(self, nivel: int) -> int:
        """
        Cuenta el número de nodos en un nivel dado del árbol.

        nivel: int
        returns: int
        """
        return self.nodos_en_nivel_rec(self.raiz, nivel, 0)

    def nodos_en_nivel_rec(self, nodo: Nodo, nivel_deseado: int, nivel_actual: int) -> int:
        if not nodo:
            return 0
        if nivel_actual == nivel_deseado:
            return 1
        cantidad_nodos = 0
        for hijo in nodo.hijos:
            cantidad_nodos += self.nodos_en_nivel_rec(hijo, nivel_deseado, nivel_actual + 1)
        return cantidad_nodos
    
    def contar_hojas(self) -> int:
        """
        Cuenta el número total de hojas en el árbol.

        returns: int
        """
        return self.contar_hojas_rec(self.raiz)

    def contar_hojas_rec(self, nodo: Nodo) -> int:
        if not nodo:
            return 0
        if not nodo.hijos:
            return 1
        cantidad_hojas = 0
        for hijo in nodo.hijos:
            cantidad_hojas += self.contar_hojas_rec(hijo)
        return cantidad_hojas

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
    print(arbol.es_hoja(indice))
    print(arbol.nodos_en_nivel(2))