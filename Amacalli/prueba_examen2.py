def repetida (lista):
    l2 = True

    if len(lista) == len(set(lista)) or not lista:
        return False
    else:
        return l2
    
if __name__ == '__main__':
    n = int(input())
    lista = []
    for _ in range(n):
        lista.append(int(input()))
    
    print(repetida(lista))