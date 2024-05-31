class Nodo():
    def __init__(self,indice,valor=None) -> None:
        self.izquierda=None #una forma para decir que aún no sabes lo que tiene la propiedad
        self.derecha=None  
        self.indice=indice
        self.valor=valor  
    def __repr__(self)->str:
        return '%s:%s'%(self.indice,self.valor)    

class Arbol_binario():
    def __init__(self):
        self.raiz=None
    
    def agregar_nodo(self,indice,valor=None):
        nuevo_nodo=Nodo(indice,valor)
        if not self.raiz:
            self.raiz=nuevo_nodo
            return
        nodo_actual=self.raiz
        while nodo_actual:
            if indice<nodo_actual.indice:
                if not nodo_actual.izquierda:
                    nodo_actual.izquierda=nuevo_nodo
                    return
                nodo_actual=nodo_actual.izquierda
            else:
                if not nodo_actual.derecha:
                    nodo_actual.derecha=nuevo_nodo
                    return
                nodo_actual=nodo_actual.derecha
        
    def regresar_valor(self,indice:int):
        nodo_actual=self.raiz
        while nodo_actual:
            if nodo_actual.indice==indice:
                return nodo_actual.valor
            if indice<nodo_actual.indice:
                nodo_actual=nodo_actual.izquierda
            else:
                nodo_actual=nodo_actual.derecha
        return None
    
    def podar(self,nodo_borrar):
        nodo_actual=self.raiz
        if not self.raiz:
            return
        while nodo_actual:
            if nodo_actual.izquierda and nodo_actual.izquierda.indice==nodo_borrar:
                nodo_actual.izquierda=None
                return
            elif nodo_actual.derecha and nodo_actual.derecha.indice==nodo_borrar:
                nodo_actual.derecha=None
                return
            if nodo_borrar<nodo_actual.indice:
                nodo_actual=nodo_actual.izquierda
            else:
                nodo_actual=nodo_actual.derecha
        self.raiz=None
        return
    
    def convertir_a_cadena_arbol_rec(self, nodo: Nodo, nivel, res) -> None:
        """
        Hace un recorrido en profundidad y convierte
        a una cadena
        """
        espacios = ''
        for i in range(nivel):
            espacios += '| '
        cadena = res[0]
        cadena += espacios + str(nodo.indice)+':'+str(nodo.valor) + '\n'
        res[0] = cadena
        while nodo:
            if nodo.izquierda:
                self.convertir_a_cadena_arbol_rec(nodo.izquierda, nivel + 1, res)
            while nodo:
                if nodo.derecha:
                    self.convertir_a_cadena_arbol_rec(nodo.derecha, nivel + 1, res)
                return
        
    def __repr__(self) -> str:
        if self.raiz==None:
            return ''
        res = ['']
        self.convertir_a_cadena_arbol_rec(self.raiz,0, res)
        return res[0].strip()


def leer_arbol(nodos: int) -> Arbol_binario:
    """
    Para leer árboles que pasa el sistema.
    Regresa el árbol resultante

    nodos: int
    returns: Arbol
    """
    arbol = Arbol_binario()
    if nodos == 0:
        return arbol
    
    for _ in range(nodos):
        cadena=input()
        if ':' in cadena:
            indice, valor = cadena.split(':')
            indice = int(indice)
            arbol.agregar_nodo(indice, valor)
        else:
            indice=int(cadena)
            arbol.agregar_nodo(indice)
    return arbol

if __name__ == '__main__':
    indice_borrar=int(input())
    nodos = int(input())
    arbol = leer_arbol(nodos)  
    arbol.podar(indice_borrar)
    print(arbol) 