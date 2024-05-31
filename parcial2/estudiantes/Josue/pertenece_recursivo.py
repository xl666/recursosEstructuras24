def pertene(x, lista):
    if not lista:
        return False
    if lista[0] == x:
        return True
    else:
        return pertene(x, lista[1:])
    
if __name__ == '__main__':
    x = int(input())
    n = int(input())    
    lista = [int(input()) for _ in range(n)]

    print(pertene(x, lista))
    