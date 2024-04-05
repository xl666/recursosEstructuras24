#XOR
#booleano1 = bool(int(input()))
#booleano2 = bool(int(input()))

#def xor(booleano1:bool, booleano2:bool):
#    if booleano1 == booleano2:
#        return False
#    return True

#print(xor(booleano1, booleano2))


#PRODUCTO
#n_elemntos = int(input())

#def leer_lista(n_elementos):
#   lista = []
#    for _ in range(n_elementos):
#        lista.append(int(input()))
#    return lista

#def calcular_producto(lista):
#    acumulador = 1
#    for elemnto in lista:
#        if elemnto == 0:
#            return 0
#        acumulador *= elemnto
#    return acumulador

#lista = leer_lista(n_elemntos)
#print(calcular_producto(lista))


# SERIE NUMERICA
posicion = int(input())

def calcular_fibonacci(posicion):
    if posicion == 1 or posicion == 2:
        return 1
    anterior = 1
    actual = 1
    for _ in range(posicion - 2):
        siguiente = anterior + actual
        anterior = actual
        actual = siguiente
    return actual
print(calcular_fibonacci(posicion))





