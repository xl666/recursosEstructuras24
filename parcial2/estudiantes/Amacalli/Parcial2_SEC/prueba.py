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
        actual = self.raiz
        while actual is not None and indice != actual.indice:
            if indice < actual.indice:
                actual = actual.izquierda
            elif indice > actual.indice:
                actual = actual.derecha
        return actual

    def convertir_a_cadena_arbol_rec(self, nodo: Nodo, prefijo, res) -> None:
        if nodo is not None:
            res[0] += f"{prefijo}{nodo.indice}:{nodo.valor}\n"
            nuevo_prefijo = prefijo + "| "
            if nodo.izquierda:
                self.convertir_a_cadena_arbol_rec(nodo.izquierda, nuevo_prefijo, res)
            if nodo.derecha:
                self.convertir_a_cadena_arbol_rec(nodo.derecha, nuevo_prefijo, res)

    def __repr__(self) -> str:
        if self.raiz is None:
            return ''
        res = ['']
        self.convertir_a_cadena_arbol_rec(self.raiz, "", res)
        return res[0].strip()

    def borrar_nodo(self, indice: int):
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
        
        self._desconectar_nodo(nodo)

        return self

    def _desconectar_nodo(self, nodo):
        if nodo is None:
            return
        
        if nodo.izquierda:
            self._desconectar_nodo(nodo.izquierda)
        if nodo.derecha:
            self._desconectar_nodo(nodo.derecha)
        nodo.padre = None
        nodo.izquierda = None
        nodo.derecha = None

def leer_arbol(nodos: int) -> Arbol_binario:
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
    arbol_bin.borrar_nodo(indice)
    print(arbol_bin)
