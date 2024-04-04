def calcular_serie(n):
    a=0
    b=1
    c=0
    for _ in range(n):
        c= a + b
        b =a
        a = c
    return a





if __name__ == '__main__':
    n=int(input())
    resultado = calcular_serie(n)
    print(resultado)
    