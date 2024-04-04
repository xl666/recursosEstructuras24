def matrix(fila , columna):
    matrix = [[int(input()) for _ in range(fila)] , [int(input()) for  _ in range(columna)]]
    return matrix
def suma_diagonal(matrix):
    suma = matrix[0][0]+matrix[1][1]
    return suma

if __name__== '__main__':
    matrix_size = int(input())
    matrix = matrix(matrix_size , matrix_size)
    suma = suma_diagonal(matrix)
    print("La suma de los elementos en la diagonal principal es: ",suma)