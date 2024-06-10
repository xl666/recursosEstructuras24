
#------------------------ Linked list ----------------------------
class Node():
    def __init__(self, data=None, prx = None):
        self.data = data
        self.prx = prx

class linkedlist():
    def __init__(self):
        self.head = None

    def insert_bg(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.prx:
            itr = itr.prx

        itr.prx = Node(data, None)

    def print(self):
        if self.head is None:
            print('')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->' 
            itr = itr.prx
    
        print(llstr)
    
    def length(self):
        cont = 0
        itr = self.head
        while itr:
            cont += 1
            itr = itr.prx

        return cont

    def remv_indx(self, indx):
        if indx < 0 or indx > self.length():
            return 'No valido'

        if indx == 0:
            self.head = self.head.next
            return

        cont = 0
        itr = self.head
        while itr:
            if cont == indx - 1:
                itr.prx = itr.prx.prx
                break

            itr = itr.prx
            cont += 1

    def insert_at(self, indx, data):
        if indx < 0 or indx >= self.length():
            return 'No valido'
        
        if indx == 0:
            self.insert_bg(data)
            return

        cont = 0
        itr = self.head

        while itr:
            if cont == indx - 1:
                node = Node(data, itr.prx)
                itr.prx = node
                break
            itr = itr.prx
            cont += 1
    
    def insert_afv(self, data_ant, data_dp):
        cont = 0
        itr = self.head
        
        while itr:
            if str(itr.data) == str(data_ant):
                node = Node(data_dp, itr.prx)
                itr.prx = node
                break

            itr = itr.prx
            cont += 1

    def rmv_value(self, data):
        if str(data) is None:
            return 'ingrese algo'

        itr = self.head
        prev = None

        while itr:
            if itr.data == data:
                if prev:
                    prev.prx = itr.prx
                else:
                    self.head = itr.prx
                break
            
            prev = itr
            itr = itr.prx
    
    def llenar_ll(self, rango):
        for i in range(rango):
            self.insert_end(int(input()))
        
#--------------------------  pila  -------------------------------
# Last In First Out

class Pila:
    def __init__(self):
        self.lista = []

    def push(self, dato):
        self.lista.append(dato)

    def pop(self):
        if not self.lista:
            return None
        return self.lista.pop()

    def peek(self):
        if not self.lista:
            return None
        return self.lista[-1]

    def inversa(self, cadena):
        for c in cadena:
            self.push(c)
        self.lista = reversed(self.lista)
        cadena_rev = ''.join(self.lista)

        return cadena_rev

    def palindromo(self, cadena):
        rev = self.inversa(cadena)
        if rev == cadena:
            return True
        else:
            return False
    
    def llenar_stack(self, cantidad):
        for n in range(cantidad):
            self.push(input())

    def ordenar(self):
        self.lista = sorted(self.lista)
        return self.lista

    def __repr__(self):
        return str(self.lista)

#-------------------------- colas --------------------------------
# First In First Out
class Cola:
    def __init__(self):
        self.lista = []

    def esta_vacia(self):
        if not self.lista:
            return True
        else:
            return False

    def append(self, dato):
        self.lista.append(dato)

    def shift(self):
        if self.esta_vacia():
            return None
        val = self.lista[0]
        self.lista = self.lista[1:]

        return val

    def peek(self):
        if self.esta_vacia():
            return None
        return self.lista[0]

    def __repr__(self):
        return str(self.lista)

    def copiar(self):
        nueva_cola = Cola()
        for elemento in self.lista:
            nueva_cola.append(elemento)
        return nueva_cola

#------------------------- Arbol general -------------------------
class Nodo():
    def __init__(self, indice):
        self.hijos = []
        self.indice = indice

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __repr__(self):
        return 'n:%s' % self.indice


class Arbol():
    """
    Implementación de un árbol general
    que guarda índices
    los índices son únicos
    """
    def __init__(self):
        self.raiz = None

    def regresarNodo_rec(self, indice, actual, resultado):
        """
        Regresa el objeto nodo con el
        índice dado
        """
        if actual.indice == indice:        
            resultado.append(actual)
            return # un poco de poda aunque sea
        
        for hijo in actual.hijos:
            self.regresarNodo_rec(indice, hijo, resultado)


    def regresarNodo(self, indice):
        res = []
        self.regresarNodo_rec(indice, self.raiz, res)
        if not res:
            return None
        return res[0]
    
        
    def agregar_hijo(self, indice, indicePadre=None):
        nuevo = Nodo(indice)
        if not self.raiz:
            self.raiz = nuevo
            return True 
        padre = self.regresarNodo(indicePadre)
        if not padre:
            return False
        padre.agregar_hijo(nuevo)
        return True

    def es_hoja(self, indice: int) -> bool:
        """
        Determina si un nodo en un índice dado es una hoja.

        self, indice: int
        returns: bool
        """
        nodo_interes = self.regresarNodo(indice)
        if not nodo_interes:
            return False
        return len(nodo_interes.hijos) == 0

    def es_padre(self, indice):
        nodo_interes = self.regresarNodo(indice)
        if not nodo_interes:
            return False
        if nodo_interes == self.raiz:
            return True

        return len(nodo_interes.hijos) > 0
        

def leer_arbol(nodos: int) -> Arbol:
    """
    Para leer árboles que pasa el sistema.
    Regresa el árbol resultante

    nodos: int
    returns: Arbol
    """
    arbol = Arbol()
    if nodos == 0:
        return arbol
    
    indice_raiz = int(input())
    arbol.agregar_hijo(indice_raiz)
    for _ in range(nodos - 1):
        nodo, padre = input().split(':')
        nodo = int(nodo)
        padre = int(padre)
        arbol.agregar_hijo(nodo, padre)

    return arbol    
    
#-------------------------Arbol BB  ------------------------------
class Nodo_():
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
        nodo_nuevo = Nodo_(indice, valor)
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
#-------------------------------------------------------------------------------------------------------

def main():
    indx = int(input())
    n_nodo = int(input())
    arbol = leer_arbol(n_nodo)
    print(arbol)

if __name__ == '__main__':
    main()

