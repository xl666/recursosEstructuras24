def obtener_pares_recursivo(lista):
    if not lista:
        return []
    if lista[0] % 2 == 0:
        return [lista[0]] + obtener_pares_recursivo(lista[1:])
    else:
        return obtener_pares_recursivo(lista[1:])

N = int(input().strip())
lista = []
for _ in range(N):
   lista.append(int(input())) 
print(obtener_pares_recursivo(lista))
