def llenar_matriz(f,c):
    matriz=[]
    for i in range(f):
        matriz.append([])
        for j in range(c):
            matriz[i].append(int(input()))
    return matriz
def suma_diagonal_inversa(matriz):
    d=len(matriz)
    sumatoria=0
    j=len(matriz)-1
    print(j)
    for i in range(d):
        sumatoria+=matriz[i][j-i]
    return sumatoria

if __name__=='__main__':
    f=int(input())
    c=int(input())
    print(suma_diagonal_inversa(llenar_matriz(f,c)))