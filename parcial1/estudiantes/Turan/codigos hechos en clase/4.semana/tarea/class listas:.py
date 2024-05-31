class Listas:
    def __init__(self,lista):
        self.lista = lista
    
    def definir(self, lista_1, lista_2):
        self.lista_1 = [i for i in range(lista_1)]
        self.lista_2 = [i for i in range(lista_2)]
        self.lista = [self.lista_1, self.lista_2]
        return self.lista
    def compara(self):
        aux = []
        for i in range(min(len(self.lista[0]), len(self.lista[1]))):
            if self.lista[0][i] == self.lista[1][i]:
                aux.append(i)
        
        return aux


if __name__ : "__main__"
lista= Listas([])
lista.definir(6,3)
print(lista.compara())        
