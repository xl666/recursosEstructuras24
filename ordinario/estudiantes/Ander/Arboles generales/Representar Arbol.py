# Crear una clase para representar un árbol general y definir métodos 
# para agregar nodos y eliminar nodos

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

    def es_hoja(self, indice: int) -> bool:
        """
        Determina si un nodo en un índice dado es una hoja.

        self, indice: int
        returns: bool
        """
        nodo_interes = self.regresarNodo(indice)
        if not nodo_interes:
            return False
        return len(nodo_interes.hijos) == 0

    def regresar_padre(self, indice: int) -> int:
        """
        Regresa el índice del padre del nodo con
        el índice dado.
        En caso de no existir o no tener padre
        se regresa None

        self,
        indice: int, índice del nodo de interés
        returns: int, índice del padre
        """
        nodo_interes = self.regresarNodo(indice)
        if not nodo_interes:
            return None
        return nodo_interes.padre.indice

    def convertir_a_cadena_arbol_rec(self, nodo: Nodo, nivel, res) -> None:
        """
        Hace un recorrido en profundidad y convierte
        a una cadena
        """
        espacios = ''
        for i in range(nivel):
            espacios += '| '
        cadena = res[0]
        cadena += espacios + str(nodo.indice) + '\n'
        res[0] = cadena 
        for hijo in nodo.hijos:
            self.convertir_a_cadena_arbol_rec(hijo, nivel + 1, res)
            
    
    def __repr__(self) -> str:
        if self.raiz == None:
            return ''
        res = ['']
        self.convertir_a_cadena_arbol_rec(self.raiz,
                                          0, res)
        return res[0].strip()

    def borrar_nodo(self, indice: int) -> None:
        """
        Borra el nodo en el índice dado de ser
        posible
        """
        if indice == self.raiz.indice:
            self.raiz = None
            return

        nodo = self.regresarNodo(indice)
        if not nodo:
            return

        nodo.padre.hijos.remove(nodo)
        

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

def es_ancestro(arbol: Arbol, indiceA: int, indiceB: int) -> bool:
    """
    Dado un objeto Arbol,
    Determina si el nodo en indiceA es ancestro
    de el nodo en el indiceB.

    arbol: Arbol, indiceA: int, indiceB: int
    returns: bool, True si A es ancestro de B
    """

    nodoB = arbol.regresarNodo(indiceB)
    if not nodoB:
        return False

    siguiente = nodoB.padre
    while siguiente != None:
        if siguiente.indice == indiceA:
            return True       
        siguiente = siguiente.padre
    return False
    


if __name__ == '__main__':
    indiceA = int(input())
    indiceB = int(input())
    n = int(input())
    arbol = leer_arbol(n)
    print(es_ancestro(arbol, indiceA, indiceB))
