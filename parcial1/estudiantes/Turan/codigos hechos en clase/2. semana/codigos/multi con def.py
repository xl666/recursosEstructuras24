def ingresar_elementos_lista(x):
    lista = []
    for _ in range(x):
        lista.append(int(input("Ingrese un número: ")))
    return lista

def multiplacion(lista):
    aux=1
    for i in range(len(lista)):
        aux=aux*lista[i]
        return aux

N_cantidad=int(input())
lista=ingresar_elementos_lista(N_cantidad)
print(lista)
resultado=multiplacion(lista)
print(resultado)