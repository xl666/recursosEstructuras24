class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente_nodo = None  # Inicialmente no hay nodo siguiente

class Lista:
    def __init__(self, valor):
        self.cabeza = Nodo(valor)  # Crear el primer nodo con el valor recibido

    def append(self, valor):
        nuevo_nodo = Nodo(valor)  # Crear un nuevo nodo con el valor recibido
        actual = self.cabeza
        while actual.siguiente_nodo is not None:
            actual = actual.siguiente_nodo
        actual.siguiente_nodo = nuevo_nodo  # Agregar el nuevo nodo al final de la lista

    def get(self, pos):
        if pos < 0:  # Verificar que la posición sea válida
            return None
        actual = self.cabeza
        indice = 0
        while actual is not None:
            if indice == pos:  # Si encontramos la posición deseada, retornar su valor
                return actual.valor
            actual = actual.siguiente_nodo
            indice += 1
        return None  # Si la posición no es encontrada, retornar None

if __name__ == "__main__":
    P = int(input())  # Posición a recuperar
    N = int(input())  # Número de elementos a leer

    lista = Lista(int(input()))  # Crear la lista con el primer valor leído
    for _ in range(N - 1):  # Leer y agregar los N-1 valores restantes a la lista
        valor = int(input())
        lista.append(valor)

    resultado = lista.get(P)  # Obtener el valor en la posición P
    print(resultado)
