def definir_lista(x):
    lista=[]
    for _ in range(x):
        lista.append(int(input()))
    return lista

def calcular_producto(y):
    acumulador=1
    for elemento in y:
        if elemento == 0:
            return 0
        acumulador *= elemento
    return acumulador
n_elementos=int(input())
lista=definir_lista(n_elementos)
print(calcular_producto(lista))