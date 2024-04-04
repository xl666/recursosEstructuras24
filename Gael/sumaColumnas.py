def leer_matriz(f,c):
    matriz =[]
    for fila in range(f):
        ff=[]
        for columna in range (c):
                ff.append(int(input()))
        matriz.append(ff)
    return matriz

def sumar_columnas(matriz):
    f=len(matriz)
    c=len(matriz[0])
    res=[0 for _ in range (c)]
    for fila in range(f):
         for columna in range(c):
              res[c]+= matriz[fila][columna]
    return res

def dar_formato(lista):
     lista_cadena = [str(ele) for ele in lista]
     return ','.join(lista_cadena)

if __name__ == '__main__':
    f=int(input())
    c = int(input())
    matriz=leer_matriz(f,c)
    print(dar_formato(sumar_columnas(matriz)))