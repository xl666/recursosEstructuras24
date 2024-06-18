#llena y recorre una matriz
def llenarmatriz(f, c):
        matriz = [] #rellenar matriz de aqui
        for _ in range(f):
            fila = []
            for i in range(c):
                fila.append(int(input()))
            matriz.append(fila) #hasta aqui

        for fila in matriz: #recorrer matriz de aqui 
             for j in fila:
                  print(j) #hasta aqui

        return matriz   


f = int(input())
c = int(input())
print(llenarmatriz(f, c))
