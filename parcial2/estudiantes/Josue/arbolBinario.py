
class Nodo():
    def __init__(self, indice, valor=None):
        self.izquierda = None
        self.derecha = None
        self.indice = indice
        self.valor = valor


    def __repr__(self) -> str:
        return '%s:%s' % (self.indice,self.valor)
        
        

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
        pass

    def __repr__(self) -> str:
        pass

    def borrar_nodo(self, indice:int) -> None:
        """
        Borra el nodo en el índice dado.

        self, indice:int
        returns: None 
        """
        pass
        
