def matrix(row):
    matrix = []
    for i in range(row):
        x = int(input())
        matrix[[0]].append(x)
        for j in range(row + 1):
            y = int(input())
4            matrix[[1]].append(y)
    print(matrix)

if __name__== '__main__':
    matrix_size = int(input())
    matrix = matrix(matrix_size)
    suma = suma_diagonal(matrix)
    print("La suma de los elementos en la diagonal principal es: ",suma)

    #Turan Ozbek


