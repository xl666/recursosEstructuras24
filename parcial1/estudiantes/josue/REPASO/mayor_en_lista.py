def mayor_lista(lista):
    if not lista:
        return None
    else:
        return max(lista)
    
if __name__ == '__main__':
    n = int(input())
    lista = []
    for _ in range(n):
        num = int(input())
        lista.append(num)

    print(mayor_lista(lista))












