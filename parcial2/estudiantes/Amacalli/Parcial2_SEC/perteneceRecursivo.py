def pertenece(numper, lista):
    if not lista:
        return False
    num = lista.pop()
    perte = pertenece(numper, lista)
    if numper == num:
        return True
    return perte

if __name__ == '__main__':
    numper = int(input())
    n_elementos = int(input())
    lista = [int(input()) for _ in range(n_elementos)]
    lista1 = lista.copy()
    print(pertenece(numper, lista1))
    
