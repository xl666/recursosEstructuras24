#plantilla del objeto
class Nodo():
    def __init__(self, indice, valor=None):
        self.izquierda = None
        self.derecha = None

        #para mantener el orden de los nodos, manera de identificar el registro
        self.indice = indice

        self.valor = valor #lo que queremos que almacene el nodo

    #regresar una cadena, todos los __ son 'especiales'
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

                #recorrido por la izquierda
                if not nodo_actual.izquierda: # si no hay nada en la izquierda
                    nodo_actual.izquierda = nodo_nuevo #se crea nodo nuevo
                    return
                nodo_actual = nodo_actual.izquierda
            else:
                #recorrido por la derecha
                if not nodo_actual.derecha: #si no hay nada en la derecha
                    nodo_actual.derecha = nodo_nuevo #se crea nodo nuevo en la derecha
                    return
                nodo_actual = nodo_actual.derecha

#recuperar valor - - - - - - -  - - - - - - - - - - - - 
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
        res = [""]
        self.convertir_a_cadena_arbol_rec(self.raiz, 0, res)
        return res[0]

    def convertir_a_cadena_arbol_rec(self, nodo: Nodo, nivel, res) -> None:
        """
        Hace un recorrido en profundidad y convierte
        a una cadena
        """
        if nodo is None:
            return
        espacios = '| ' * nivel  # dar formato de árbol
        cadena = res[0]
        cadena += espacios + str(nodo.indice) + '\n'
        res[0] = cadena
        self.convertir_a_cadena_arbol_rec(nodo.izquierda, nivel + 1, res)
        self.convertir_a_cadena_arbol_rec(nodo.derecha, nivel + 1, res)


#borrar el nodo - - -  - - - - - - - - - - - - - - - - 
    def borrar_nodo(self, indice:int) -> None:
        """
        Borra el nodo en el índice dado.

        self, indice:int
        returns: None 
        """
        pass

if __name__ == '__main__':
    indice_v = int(input())
    nodos = int(input())
    arbol = leer_arbol(nodos)
    print(arbol)  