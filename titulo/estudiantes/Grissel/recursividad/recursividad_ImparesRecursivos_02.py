# Solucion con ayuda de Jorge 
def impares(n, x = 1, suma = 0):
    if x <= n:
        num = x % 2
        if num != 0:
            suma = suma + x
        suma = impares(n, x + 1, suma)
    return suma

if __name__ == '__main__':
    n = int(input())
    res = impares(n)
    print(res)