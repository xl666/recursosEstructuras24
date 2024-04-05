
def Producto(lista):
    res = lista[0]
    for elemento in lista:
        res = elemento * res
    
    return res

if __name__ == '__main__':
    Entrada = int(input())
    lista = []

    for i in range(Entrada):
        lista.append(int(input()))
    
    print(Producto(lista))