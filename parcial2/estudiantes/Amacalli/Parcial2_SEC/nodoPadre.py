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
        """
        if self.raiz is None:
            return False

        nodo = self.regresarNodo(indice)

        if nodo.hijos:
            return False
        return True
    
    def nodo_Padre(self, indice: int) -> int:
        nodo_interes = self.regresarNodo(indice)
        if not nodo_interes:
            return None
        padre = nodo_interes.padre
        if not padre:
            return None
        return padre.indice
    
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
        self.convertir_a_cadena_arbol_rec(self.raiz, 0, res)
        return res[0].strip()
    
    def borrarNodo_arbol(self, indice: int) -> str:
        """
        Revisa que el indice que se ingresó pertenezca al arbol
        si está lo elmina y retorna el arbol resultante
        """
        nodo = self.regresarNodo(indice)
        
        if not nodo:
            return 
        
        if nodo == self.raiz:
            self.raiz == None
            return 
        
        padre = nodo.padre

        for hijo in padre.hijos:
            if hijo == nodo:
                padre.hijos.remove(hijo)

        return arbol
    
    def ancestro_rec(self, indiceA: Nodo, indiceB: Nodo) -> bool:
        """
        Recibe dos nodos y se verifica si el indiceB es igual al indiceA
        si no toma el padre del indiceB y lo manda para hacer un llamada recusiva
        """
        if indiceA == indiceB:
            return True
        
        padre = indiceB.padre
        
        if padre == None:
            return False
        
        return self.ancestro_rec(indiceA, padre)
    
    def ancestro(self, indiceA: int, indiceB: int) -> bool:
        """
        Llama a la función recursiva, pero antes revisa que ambos indices
        se encuentren en el arbol
        """
        nodoA = self.regresarNodo(indiceA)
        nodoB = self.regresarNodo(indiceB)
        if not nodoA or not nodoB:
            return False

        return self.ancestro_rec(nodoA, nodoB)

def leer_arbol(nodos: int) -> Arbol:
    """
    Para leer árboles que pasa el sistema.
    Regresa el árbol resultante
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
    indiceA = int(input())
    #indiceB = int(input())
    nodos = int(input())
    arbol = leer_arbol(nodos)   
    print(arbol.nodo_Padre(indiceA))