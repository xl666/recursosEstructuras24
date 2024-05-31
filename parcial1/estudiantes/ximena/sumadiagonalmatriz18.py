#Dada una matriz cuadra (tiene el mismo número de filas que columnas), regresa la suma de los elementos que se encuentran en la diagonal.
#Ejemplo de entrada
#2,2
#1,1
#2,2
#Ejemplo de salida
#3
def suma_diagonal(F, C, matriz):
    if F != C or len(matriz) != F:
        return None
    
    suma_diagonal = 0 

    for i in range(F):
        suma_diagonal += matriz[i][i]
    return suma_diagonal

def matrizfinal(F, C):
    matriz = []
    for i in range(F):
        fila = []
        for j in range(C):
            elemento = int(input())
            fila.append(elemento)
        matriz.append(fila)
    return matriz

F = int(input())
C = int(input())
matriz = matrizfinal(F, C) 
resultado = suma_diagonal(F, C, matriz)
print(resultado)