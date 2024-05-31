class Nodo():
    def __init__(self, indice, padre=None):
        self.hijos = []
        self.indice = indice
        self.padre = padre

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __repr__(self):
        return 'n:%s' % self.indice


class Arbol():
    def __init__(self):
        self.raiz = None

    def regresarNodo_rec(self, indice, actual, resultado):
        if actual.indice == indice:
            resultado.append(actual)
            return
        for hijo in actual.hijos:
            self.regresarNodo_rec(indice, hijo, resultado)

    def regresarNodo(self, indice):
        res = []
        if self.raiz:
            self.regresarNodo_rec(indice, self.raiz, res)
        if not res:
            return None
        return res[0]

    def eliminar_nodo(self, indice):
        nodo_a_borrar = self.regresarNodo(indice)
        if not nodo_a_borrar:
            return False

        if nodo_a_borrar.padre:
            nodo_a_borrar.padre.hijos.remove(nodo_a_borrar)
        else:
            self.raiz = None
        return True
    
    def agregar_hijo(self, indice, indicePadre=None):
        if not self.raiz:
            nuevo = Nodo(indice)
            self.raiz = nuevo
            return True
        padre = self.regresarNodo(indicePadre)
        if not padre:
            return False
        nuevo = Nodo(indice, padre)
        padre.agregar_hijo(nuevo)
        return True

    def convertir_a_cadena_arbol_rec(self, nodo, nivel, res):
        espacios = '| ' * nivel
        res.append(espacios + str(nodo.indice))
        for hijo in nodo.hijos:
            self.convertir_a_cadena_arbol_rec(hijo, nivel + 1, res)

    def __repr__(self):
        if not self.raiz:
            return ""
        res = []
        self.convertir_a_cadena_arbol_rec(self.raiz, 0, res)
        return '\n'.join(res)


def leer_arbol(nodos):
    arbol = Arbol()
    if nodos == 0:
        return arbol

    indice_raiz = int(input().strip())
    arbol.agregar_hijo(indice_raiz)
    for _ in range(nodos - 1):
        entrada = input().strip().split(':')
        nodo = int(entrada[0])
        padre = int(entrada[1])
        arbol.agregar_hijo(nodo, padre)

    return arbol


if __name__ == '__main__':
    indice = int(input().strip())
    nodos = int(input().strip())
    arbol = leer_arbol(nodos)
    arbol.eliminar_nodo(indice)
    print(arbol)
