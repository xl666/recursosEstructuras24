class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Lista():
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self): #si está vacía, el append no funciona
        return self.cabeza==None

    def append(self, valor):
        nuevo=Nodo(valor)
        # caso especial lista vacía
        if self.esta_vacia():
            self.cabeza=nuevo 
            return #regresa None
        # la lista no está vacía:
        aux = self.cabeza
        while aux.siguiente != None:
            aux = aux.siguiente
        aux.siguiente=nuevo

    def get(self, pos):
        if self.esta_vacia():
            return None
        if pos <0:
            return None
        cont=0
        aux=self.cabeza
        while cont < pos:
            cont+=1
            aux =aux.siguiente
            if not aux:
                return None
        return aux.valor


if __name__ == '__main__':
    p = int(input())
    n = int(input())
    l = Lista()
    for _ in range(n):
        l.append(int(input()))

    print(l.get(p))
