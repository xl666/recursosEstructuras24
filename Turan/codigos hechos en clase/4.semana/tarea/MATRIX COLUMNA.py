def matrix(f, c):
    matrix =[]
    for i in range(f):
        row = []
        for  j in range(c):
            row.append(int(input()))
        matrix.append(row)    
    return matrix

def sum(matrix):
    sumlista=[]
    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]
        sumlista.append(sum)
    return sumlista

if  __name__ == '__main__':
    f= int(input())
    c= int(input())
    build_it= matrix(f, c)
    sum= sum(build_it)
    sum =','.join(map(str, sum))
    #sum1 = ','.join(str(_) for _ in sum)
    print(sum)