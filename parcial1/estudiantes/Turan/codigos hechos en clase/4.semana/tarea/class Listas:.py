class Listas:
    def __init__(self,lista):
        self.lista = lista

    def definir(self,long_lista_1,long_lista_2):
        self.lista1 = []
        self.lista2 = []
        for i in range(long_lista_1):
            i = int(input())
            self.lista1.append(i)
        for i in range(long_lista_2):
            i = int(input())
            self.lista2.append(i)
        self.lista = [lista1,lista2]
        return self.lista
    def compara(self):
        aux = []
        for i in range(self.lista):
            if self.lista[0][i] == self.lista[1][i]:
                aux.append(i)
        return aux
    
if __name__=='__main__':    
    long_lista_1 = int(input())
    long_lista_2 = int(input())
    Listas.definir(long_lista_1 , long_lista_2)
    print(Listas.compara())

