class Nodo():
    def __init__(self, indice, padre=None):
        self.hijos = []
        self.indice = indice
        self.padre = padre

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __repr__(self):
        return str(self.indice)

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
        if not nodo_interes or not nodo_interes.padre:
            return None
        return nodo_interes.padre.indice

    def convertir_a_cadena_arbol_rec(self, nodo: Nodo, nivel, res) -> None:
        """
        Hace un recorrido en profundidad y convierte
        a una cadena
        """
        espacios = '| ' * nivel
        cadena = res[0]
        cadena += espacios + str(nodo.indice) + '\n'
        res[0] = cadena 
        for hijo in nodo.hijos:
            self.convertir_a_cadena_arbol_rec(hijo, nivel + 1, res)
    
    def borrar_nodo(self, indice):
        nodo = self.regresarNodo(indice)
        if not nodo:
            return False
        if nodo.padre:
            nodo.padre.hijos.remove(nodo)
        else:
            self.raiz = None
        return True
            
    def __repr__(self) -> str:
        res = ['']
        self.convertir_a_cadena_arbol_rec(self.raiz, 0, res)
        return res[0].strip()
    
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
    arbol.borrar_nodo(indice)
    print(arbol)  

#Pasos a seguir para borrar el nodo indicado
 #   - encontrar nodos
  #  - situar padre con ayuda de la funcion ya creada de padre
   # - utilizar del o remove y borrar