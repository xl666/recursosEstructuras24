def definir_lista(cantidad):
    t1 = 0
    t2 = 1
    lista = [1]
    for _ in range(cantidad-1):
        next = t1 + t2
        lista.append(next)
        t1 = t2
        t2 = next
        print(lista)
    return next

N_numero = int(input())
resultado = definir_lista(N_numero)
print(resultado)
