# plantilla del objeto
class Nodo():
    def __init__(self, indice, valor=None):
        self.izquierda = None
        self.derecha = None

        # para mantener el orden de los nodos, manera de identificar el registro
        self.indice = indice

        self.valor = valor # lo que queremos que almacene el nodo

    # regresar una cadena, todos los __ son 'especiales'
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
                # recorrido por la izquierda
                if not nodo_actual.izquierda: # si no hay nada en la izquierda
                    nodo_actual.izquierda = nodo_nuevo # se crea nodo nuevo
                    return
                nodo_actual = nodo_actual.izquierda
            else:
                # recorrido por la derecha
                if not nodo_actual.derecha: # si no hay nada en la derecha
                    nodo_actual.derecha = nodo_nuevo # se crea nodo nuevo en la derecha
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
            if nodo_actual.indice == indice:
                return nodo_actual.valor
            elif indice < nodo_actual.indice:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
        return None

    def __repr__(self) -> str:
        pass

    def borrar_nodo(self, indice:int) -> None:
        """
        Borra el nodo en el índice dado.

        self, indice:int
        returns: None 
        """
        pass

def leer_arbol(nodos):
    arbol = Arbol_binario()
    for _ in range(nodos):
        entrada = input().strip()
        indice, valor = entrada.split(':')
        arbol.agregar_nodo(int(indice), valor)
    return arbol

if __name__ == '__main__':
    indice = int(input())
    nodos = int(input())
    arbol = leer_arbol(nodos)
    print(arbol.regresar_valor(indice))
