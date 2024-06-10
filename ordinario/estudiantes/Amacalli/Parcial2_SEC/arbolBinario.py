class Nodo:
    def __init__(self, indice, valor=None, padre=None):
        self.izquierda = None
        self.derecha = None
        self.indice = indice
        self.valor = valor
        self.padre = padre

    def __repr__(self) -> str:
        return f'{self.indice}:{self.valor}'

class Arbol_binario:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, indice, valor=None):
        if not self.raiz:
            self.raiz = Nodo(indice, valor)
            return

        nodo_actual = self.raiz
        while nodo_actual:
            padre = nodo_actual
            if indice < nodo_actual.indice:
                if not nodo_actual.izquierda:
                    nodo_actual.izquierda = Nodo(indice, valor, padre)
                    return
                nodo_actual = nodo_actual.izquierda
            else:  # por derecha
                if not nodo_actual.derecha:
                    nodo_actual.derecha = Nodo(indice, valor, padre)
                    return
                nodo_actual = nodo_actual.derecha

    def regresar_valor(self, indice: int) -> Nodo:
        """
        Regresa el valor en el índice dado.
        None si no existe el índice

        self, indice
        returns: str 
        """
        actual = self.raiz
        while actual is not None and indice != actual.indice:
            if indice < actual.indice:
                if not actual.izquierda:
                    None
                actual = actual.izquierda
            elif indice > actual.indice:
                if not actual.derecha:
                    return None
                actual = actual.derecha
        return actual

    def convertir_a_cadena_arbol_rec(self, nodo: Nodo, nivel, res) -> None:
        """
        Se hace un recorrido del arbol y se convierte a cadena
        """
        espacios = ''
        for i in range(nivel):
            espacios += '| '
        cadena = res[0]
        cadena += espacios + str(nodo.indice) + ':' + str(nodo.valor) + '\n'
        res[0] = cadena 
        if nodo.izquierda:
            self.convertir_a_cadena_arbol_rec(nodo.izquierda, nivel + 1, res)  
        if nodo.derecha:
            self.convertir_a_cadena_arbol_rec(nodo.derecha, nivel + 1, res)

    def __repr__(self) -> str:
        if self.raiz is None:
            return ''
        res = ['']
        self.convertir_a_cadena_arbol_rec(self.raiz, 0, res)
        return res[0].strip()

    def borrar_nodo(self, indice: int):
        """
        Borra el nodo en el índice dado.

        self, indice:int
        returns: None 
        """
        nodo = self.regresar_valor(indice)
        if not nodo:
            return self

        if nodo == self.raiz:
            self.raiz = None
            
        else:
            if nodo.padre.izquierda == nodo:
                nodo.padre.izquierda = None
            elif nodo.padre.derecha == nodo:
                nodo.padre.derecha = None

        return arbol_bin

def leer_arbol(nodos: int) -> Arbol_binario:
    """
    Para leer árboles que pasa el sistema.
    Regresa el árbol resultante
    """
    arbol_bin = Arbol_binario()
    if nodos == 0:
        return arbol_bin
    
    for _ in range(nodos):
        nodo, valor = input().split(':')
        nodo = int(nodo)
        arbol_bin.agregar_nodo(nodo, valor)

    return arbol_bin

if __name__ == '__main__':
    indice = int(input())
    nodos = int(input())
    arbol_bin = leer_arbol(nodos) 
    print(arbol_bin)
