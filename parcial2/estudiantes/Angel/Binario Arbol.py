class Nodo:
    def __init__(self, indice, valor=None):
        self.izquierda = None
        self.derecha = None
        self.indice = indice
        self.valor = valor

    def __repr__(self) -> str:
        return f"{self.indice}:{self.valor}"

class Arbol_binario:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, entrada):
        indice, valor = entrada.split(':')
        indice = int(indice)
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
            else:
                if not nodo_actual.derecha:
                    nodo_actual.derecha = nodo_nuevo
                    return
                nodo_actual = nodo_actual.derecha

    def eliminar_nodo(self, raiz, indice):
        if raiz is None:
            return raiz

        if indice < raiz.indice:
            raiz.izquierda = self.eliminar_nodo(raiz.izquierda, indice)
        elif indice > raiz.indice:
            raiz.derecha = self.eliminar_nodo(raiz.derecha, indice)
        else:
            if raiz.izquierda is None:
                return raiz.derecha
            elif raiz.derecha is None:
                return raiz.izquierda

            nodo_sucesor = self.obtener_minimo(raiz.derecha)
            raiz.indice = nodo_sucesor.indice
            raiz.valor = nodo_sucesor.valor
            raiz.derecha = self.eliminar_nodo(raiz.derecha, nodo_sucesor.indice)
        return raiz
    def eliminar(self, indice):
        indice = int(indice)
        self.raiz = self.eliminar_nodo(self.raiz, indice)

    def eliminar_nodo(self, raiz, indice):
        if raiz is None:
            return raiz

        if indice < raiz.indice:
            raiz.izquierda = self.eliminar_nodo(raiz.izquierda, indice)
        elif indice > raiz.indice:
            raiz.derecha = self.eliminar_nodo(raiz.derecha, indice)
        else:
            return None
        return raiz
    
    def buscar_valor(self, indice):
        indice = int(indice)  
        nodo_actual = self.raiz
        while nodo_actual:
            if indice == nodo_actual.indice:
                return nodo_actual.valor
            elif indice < nodo_actual.indice:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
        return nodo_actual

    def convertir_a_cadena_arbol_rec(self, nodo, nivel, res):
        if nodo is None:
            return
        espacios = "| " * nivel
        cadena = res[0]
        cadena += f"{espacios}{nodo}\n"
        res[0] = cadena
        if nodo.izquierda:
            self.convertir_a_cadena_arbol_rec(nodo.izquierda, nivel + 1, res)
        if nodo.derecha:
            self.convertir_a_cadena_arbol_rec(nodo.derecha, nivel + 1, res)

    def imprimir_arbol(self):
        res = [""]
        if self.raiz:
            self.convertir_a_cadena_arbol_rec(self.raiz, 0, res)
        print(res[0].strip())

    def valor_existe(self, valor: int) -> bool:
        """
        Verifica si un valor dado existe en el árbol.

        valor: int
        returns: bool
        """
        return self.valor_existe_rec(self.raiz, valor)

    def valor_existe_rec(self, nodo: Nodo, valor: int) -> bool:
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        return self.valor_existe_rec(nodo.izquierda, valor) or self.valor_existe_rec(nodo.derecha, valor)
    
    def maximo_valor(self) -> int:
        """
        Encuentra el valor máximo en el árbol.

        returns: int
        """
        if self.raiz is None:
            return None
        nodo_actual = self.raiz
        while nodo_actual.derecha:
            nodo_actual = nodo_actual.derecha
        return nodo_actual.valor 
       
    def es_arbol_perfecto(self) -> bool:
        """
        Verifica si el árbol es un árbol binario perfecto.

        returns: bool
        """
        altura = self.altura()
        nodos = self.contar_nodos()
        return nodos == 2 ** altura - 1
if __name__ == '__main__':
    arbol = Arbol_binario()
    #indice = input()

    n = int(input())  
    entradas = []
    for nodos in range(n):
        entrada = input()
        entradas.append(entrada)
    

    for entrada in entradas:
        arbol.agregar_nodo(entrada)

    arbol.imprimir_arbol() 

    #arbol.eliminar(indice)  
    #arbol.imprimir_arbol()  

    #print(arbol.buscar_valor(indice)) 

    
