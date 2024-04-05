# - - - - NUMERO MAYOR - - - -
def elemento_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor 

if __name__ == '__main__':
    n = int(input())
    if n > 0:
        numeros = [int(input()) for _ in range (n)]
        mayor = elemento_mayor(numeros)
        print(mayor)
         