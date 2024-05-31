class Nodo():
    def __init__(self, indice, valor=None):
        self.izquierda = None
        self.derecha = None
        self.indice = indice
        self.valor = valor

    def __repr__(self) -> str:
        return '%s:%s' % (self.indice, self.valor)
        

class Arbol_binario():
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, indice, valor=None):
        nodo_nuevo = Nodo(indice, valor)
        if not self.raiz:            
            self.raiz = nodo_nuevo
            return

        nodo_actual = self.raiz
        while nodo_actual:
            if indice < nodo_actual.indice:
                if not nodo_actual.izquierda:
                    nodo_actual.izquierda = nodo_nuevo
                    return
                nodo_actual = nodo_actual.izquierda
            else: # por derecha
                if not nodo_actual.derecha:
                    nodo_actual.derecha = nodo_nuevo
                    return
                nodo_actual = nodo_actual.derecha

    def regresar_valor(self, indice: int) -> str:
        """
        Regresa el valor en el índice dado.
        None si no existe el índice

        self, indice
        returns: str 
        """
        nodo_actual = self.raiz
        while nodo_actual:
            if indice == nodo_actual.indice:
                return nodo_actual.valor
            elif indice < nodo_actual.indice:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
        return None

    def __repr__(self) -> str:
        nodos = []
        self._inorden(self.raiz, nodos)
        return ' '.join(str(nodo) for nodo in nodos)

    def _inorden(self, nodo, nodos):
        if nodo:
            self._inorden(nodo.izquierda, nodos)
            nodos.append(nodo)
            self._inorden(nodo.derecha, nodos)

    def borrar_nodo(self, indice:int) -> None:
        """
        Borra el nodo en el índice dado.

        self, indice:int
        returns: None 
        """
        self.raiz = self._borrar_nodo_rec(self.raiz, indice)

    def _borrar_nodo_rec(self, nodo, indice):
        if nodo is None:
            return nodo
        
        if indice < nodo.indice:
            nodo.izquierda = self._borrar_nodo_rec(nodo.izquierda, indice)
        elif indice > nodo.indice:
            nodo.derecha = self._borrar_nodo_rec(nodo.derecha, indice)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            
            nodo_temp = self._min_value_node(nodo.derecha)
            nodo.indice = nodo_temp.indice
            nodo.valor = nodo_temp.valor
            nodo.derecha = self._borrar_nodo_rec(nodo.derecha, nodo_temp.indice)

        return nodo

    def _min_value_node(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual