def matrix(f, c):
    matrix =[]
    for i in range(f):
        row = []
        for  j in range(c):
            row.append(int(input()))
        matrix.append(row)    
    return matrix

def sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum

if  __name__ == '__main__':
    f= int(input())
    c= int(input())
    build_it= matrix(f, c)
    #sum= sum(build_it)
    print(sum(build_it))