# Escribir una función para calcular la altura de un árbol binario.

class Nodo():
    def __init__(self, indice, valor=None):
        self.izquierda = None
        self.derecha = None
        self.indice = indice
        self.valor = valor


    def __repr__(self) -> str:
        return '%s:%s' % (self.indice,
                          self.valor)
        
        

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
        if not self.raiz:
            return None
        actual = self.raiz
        while actual.indice != indice:
            if indice < actual.indice:
                if not actual.izquierda:
                    return None
                actual = actual.izquierda
            else:
                if not actual.derecha:
                    return None
                actual = actual.derecha
        return actual.valor


    def imprimir_arbol_rec(self, nodo, nivel, res):        
        espacios = ''
        for i in range(nivel):
            espacios += '| '
        cadena = res[0]
        cadena += espacios + str(nodo.indice) + ':' + str(nodo.valor) + '\n'
        res[0] = cadena

        if nodo.izquierda:
            self.imprimir_arbol_rec(nodo.izquierda,
                                    nivel +1,
                                    res)

        if nodo.derecha:
            self.imprimir_arbol_rec(nodo.derecha,
                                    nivel +1,
                                    res)
    
    def __repr__(self) -> str:
        res = ['']
        self.imprimir_arbol_rec(self.raiz, 0, res)
        return res[0]

    def borrar_nodo(self, indice:int) -> None:
        """
        Borra el nodo en el índice dado.

        self, indice:int
        returns: None 
        """
        if indice == self.raiz.indice:
            self.raiz = None
            return
        nodo = self.raiz
        while True:
            # Encontré el nodo que quiero borrar por la izquierda
            if nodo.izquierda and nodo.izquierda.indice == indice:
                nodo.izquierda = None
                return
            # Encontré el nodo que quiero borrar por la derecha
            if nodo.derecha and nodo.derecha.indice == indice:
                nodo.derecha = None
                return
            # Todavía no encuentro el nodo, voy a ver si voy por izquierda
            if indice < nodo.indice:
                if not nodo.izquierda:
                    return
                nodo = nodo.izquierda
            # Todavía no encuentro el nodo, voy a ver si voy por derecha
            else:
                if not nodo.derecha:
                    return
                nodo = nodo.derecha

    def contar_niveles_rec(self, nodo):
        if nodo is None:
            return 0
        izquierda = self.contar_niveles_rec(nodo.izquierda)
        derecha = self.contar_niveles_rec(nodo.derecha)
        return max(izquierda, derecha) + 1

    def contar_niveles(self):
        return self.contar_niveles_rec(self.raiz)

                
        

def leer_arbol(n: int) -> Arbol_binario:
    """
    Regresa un árbol de acuerdo a como lo pasa
    el sistema
    """
    arbol = Arbol_binario()
    for _ in range(n):
        partes = input().split(':')
        indice = int(partes[0])
        valor = partes[1]
        arbol.agregar_nodo(indice, valor)
    return arbol

if __name__ == '__main__':
    v = int(input())
    n = int(input())
    arbol = leer_arbol(n)
    print(arbol.contar_niveles())
    print(arbol)
    
