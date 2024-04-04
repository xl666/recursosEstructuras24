def llenar_matriz (filas,columnas):
    res=[]
    for _ in range(filas):
        res.append([])
        for i in range (columnas):
            res[_].append(int(input()))
    return res
def suma_columna(matriz):
    aux=[0]*max(len(fila) for fila in matriz)
    for fila in matriz:
        for columna in range (len(fila)):
                aux[columna]+=fila[columna]
    for i in range(len(aux)):
         aux[i]=str(aux[i])
    return ','.join(aux)
if __name__=='__main__':
    filas=int(input())
    columnas=int(input())
    matriz=llenar_matriz(filas,columnas)
    sumatoria=suma_columna(matriz)
    print(sumatoria)