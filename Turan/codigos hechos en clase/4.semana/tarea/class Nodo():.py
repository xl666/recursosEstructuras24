class Nodo():
    def __init__(self,valor):
        self.valor = valor
        self.siguente = None
class Lista():
    def __init__(self,valor):
        self.cabeza = None

    def append(self,valor):
        nuevo_nodo = Nodo(valor)
        actual = self.cabeza
        while nuevo_nodo != None:
            actual = actual.siguiente_nodo
            actual.siguente_nodo = nuevo_nodo


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
        return None

if __name__ : '__main__'
    p = int(input())
    n = int(input())
    l = Lista()
    for in range(n-1)
    valor = int(input())
    lista.append(valor)
        
 resultado = lista.get(P)  # Obtener el valor en la posición P
    print(resultado)

