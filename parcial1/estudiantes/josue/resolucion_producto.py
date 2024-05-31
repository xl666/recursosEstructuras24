n_elementos = int(input())

def leer_lista(n_elementos):
    lista = []
    for _ in range(n_elementos):
        lista.append(int(input()))
    return lista
    
def calcular_producto(lista):
    acumulador = 1
    for elemento in lista:
        if elemento == 0:
            return 0
        acumulador *= elemento
    return acumulador

lista = leer_lista(n_elementos)
print(calcular_producto(lista))