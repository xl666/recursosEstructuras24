def llenar_matriz(f,c):
    res=[]
    for i in range(f):
        res.append([])
        for j in range(c):
            res[i].append(int(input()))
    return res

def sumar_filas(matriz):
    sumatorias=[]
    for fila in matriz:
        acumulado=0
        for columna in fila:
            acumulado+=columna
        sumatorias.append(str(acumulado))
    return ','.join(sumatorias)
if __name__=='__main__':
    f=int(input())
    c=int(input())
    print(sumar_filas(llenar_matriz(f,c)))