def pertene_rec(x, lista):
    if not lista:
        return False
    if lista[0] == x:
        return True
    else:
        return pertene_rec(x, lista[1:])

if __name__ == '__main__':
    x = int(input())
    n = int(input())
    lista = []
    
    for _ in range(n):
        valor = int(input())
        lista.append(valor)

    print(pertene_rec(x, lista))

