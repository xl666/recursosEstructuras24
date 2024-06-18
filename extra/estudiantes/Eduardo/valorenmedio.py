
def valormedio(f, c):
        matriz = [] 
        for _ in range(f):
            fila = []
            for i in range(c):
                fila.append(int(input()))
            matriz.append(fila)
        enmedio = len(matriz) // 2
        return matriz[enmedio][enmedio]

f = int(input())
c = f
print(valormedio(f, c))
