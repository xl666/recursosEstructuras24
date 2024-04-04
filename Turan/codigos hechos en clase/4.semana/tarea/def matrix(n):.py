def matrix(n):
    matrix = []
    for i in range(n):
        row =[]
        for j in range(n):
            row.append(int(input()))
        matrix.append(row)
    return matrix

def sum_of_elements(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total



if  __name__ == "__main__":
    n = int(input("Enter the size of the square matrix:"))
    buildit = matrix(n)
    total= sum_of_elements(buildit)
    print(total)

    #Turan Ozbek