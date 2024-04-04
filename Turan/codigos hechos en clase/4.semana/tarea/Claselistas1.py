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
        self.lista = [self.lista1,self.lista2]
        return self.lista
    def compara(self):
        aux = []
        for i in self.lista[0]:
            if i in self.lista[1]:
                aux.append(i)
        sorted(list(set(aux)))
        return aux
    
if __name__=='__main__':    
    longtitud_lista_1 = int(input())
    longtitud_lista_2 = int(input())
    listas_obj = Listas([])
    listas_obj.definir(longtitud_lista_1,longtitud_lista_2)
    resultado =(listas_obj.compara())
    print(resultado)
