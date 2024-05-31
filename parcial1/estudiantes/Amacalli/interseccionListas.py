class Listas:
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2
        
    def comparacion(self):
        listaf = []
        for elemento in self.lista1:
            if elemento in self.lista2:
                listaf.append(elemento)
        listaf.sort()
        return listaf
    
    def eliminar_iguales(self, listaf):
        listat = []
        for i in range(len(listaf) - 1):
            if listaf[i] != listaf[i + 1]:
                listat.append(listaf[i])

        if listaf and listaf[-1] != listaf[-2]:
            listat.append(listaf[-1])
        return listat

         
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    lista1 = []
    lista2 = []
    for _ in range(n):
        lista1.append(int(input()))

    for _ in range(m):
        lista2.append(int(input()))

    if len(lista1) == len(lista2):
        comparar = Listas(lista1, lista2)
        comun = comparar.comparacion()
        comun2 = comparar.eliminar_iguales(comun)
        print(comun2)