class Nodo():
    def __init__(self,valor):
        self.valor=valor
        self.siguiente=None

class Lista():
    def __init__(self,valor):
        self.cabeza=None
    def append (self,valor):
        nuevo_nodo= Nodo(valor)
        aux=self.cabeza
        while aux.siguiente!=None:
            aux=aux.siguiente
    def get(self,pos):
        if pos<0:
            return None
        actual=self.cabeza
        for _ in range(pos):
            if actual is None:
                return None
            actual=actual.siguiente_nodo

if __name__=='__main__':
    p=int(input())
    n=int(input())
    
    lista=Lista(valor[0])
    for _ in range(n):
        lista=lista.append(int(input()))
    print(lista.get(p))