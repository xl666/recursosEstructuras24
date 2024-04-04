def llenar_matriz (filas,columnas):
    res=[]
    for _ in range(filas):
        res.append([])
        for i in range (columnas):
            res[_].append(int(input()))
    return res

def suma_diagonal(matriz):
    aux=0
    for fila in range (len(matriz)):
        for columna in range (len(matriz[fila])):
            if fila==columna:
                aux+=matriz[fila][columna]
    return aux         

if __name__=='__main__':
    filas=int(input())
    columnas=int(input())
    matriz=llenar_matriz(filas,columnas)
    sumatoria=suma_diagonal(matriz)
    print(sumatoria)