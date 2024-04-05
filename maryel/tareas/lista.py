n_elementos = int(input())

def leer_lista(n_elementos):
    lista = []
    for _ in range (n_elementos):
        lista.append(int(input()))
    return lista
print (leer_lista(n_elementos)) 