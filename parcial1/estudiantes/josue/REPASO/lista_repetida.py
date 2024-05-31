def todos_se_repiten_al_menos_una_vez(lista):
    # Convertir la lista en un conjunto para eliminar duplicados
    conjunto = set(lista)
    print(len(lista))
    print(len(conjunto))
    # Si la longitud del conjunto es igual a la longitud de la lista original,
    # significa que todos los elementos son únicos y no se repiten al menos una vez
    return len(conjunto) != len(lista)

if __name__ == "__main__":
    n = int(input())
    lista = []
    for _ in range(n):
        lista.append(int(input()))
    resultado = todos_se_repiten_al_menos_una_vez(lista)
    print(resultado)
