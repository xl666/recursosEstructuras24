def eliminar_repetidos(lista, elementos):
    if not elementos:
        return []
    sin_repetidos = list(set(lista))
    if len(lista) > len(sin_repetidos):
        return sin_repetidos
    else:
        return eliminar_repetidos(set(lista), elementos)


if __name__ == "__main__":
    elementos = int(input())
    lista = [int(input()) for _ in range(elementos)]
    print(eliminar_repetidos(lista, elementos))
