N_cantidad=int(input())
lista=[]
for _ in range(N_cantidad):
    lista.append(int(input()))
#print(lista)
aux=1
for i in range(len(lista)):
    aux=aux*lista[i]

resultado=aux
print(resultado)

# version de maestro


def definir_lista(x):
    lista=[]
    for _ in range(n_elementos)
        lista.append(int(input()))
    return lista

def calcular_producto(y):
    acumulador=1
    for elemento in y:
        if elemento == 0:
            return 0
        acumulador *= elementor
    return acumulador