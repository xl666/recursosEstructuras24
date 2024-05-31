def repetida (lista):
    res = 0
    for i in range(len(lista)):
        if lista[i] in lista:
            res += 2
            if res > 2:
                return True
            else:
                return False
    
if __name__ == '__main__':
    n = int(input())
    lista = []
    for _ in range(n):
        lista.append(int(input()))
    
    print(repetida(lista))