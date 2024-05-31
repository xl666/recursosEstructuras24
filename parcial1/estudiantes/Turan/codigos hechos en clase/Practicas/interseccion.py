class Listas:
    def __init__(self,lista):
        self.lista = lista
    
    def comun(self,other):
       intersection = self.lista.intersection(other.lista)
       return intersection
    
    def __repr__(self):
        return self.lista


if __name__== '__main__':
    n = int(input())
    m = int(input())
    l1 = set([int(input()) for num in range(n)])
    l2 = set([int(input()) for num in range(m)])
    result = list(Listas(l1).comun(Listas(l2)))
    result.sort()
    print(result)
    