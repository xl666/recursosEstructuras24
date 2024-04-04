class Nodo:
    def _init_(self, elemento):
        self.elemento = elemento
        self.siguiente_nodo = None

class Lista:
    def _init_(self, elemento):
        self.cabeza = Nodo(elemento)

    def agregar_elemento(self, elemento):
        nuevo_nodo = Nodo(elemento)
        actual = self.cabeza

        while actual.siguiente_nodo is not None:
            actual = actual.siguiente_nodo

        actual.siguiente_nodo = nuevo_nodo

    def obtener_elemento(self, posicion):
        if posicion < 0:
            return None

        actual = self.cabeza
        for i in range(posicion):
            if actual is None:
                return None
            actual = actual.siguiente_nodo

        if actual is not None:
            return actual.elemento
        else:
            return None

if __name__=='__main__':
    P = int(input())
    N = int(input())
    elementos = [int(input()) for _ in range(N)]

    mi_lista = Lista(elementos[0])

    for i in range(1, N):
        mi_lista.agregar_elemento(elementos[i])

    resultado = mi_lista.obtener_elemento(P)
    print(resultado)