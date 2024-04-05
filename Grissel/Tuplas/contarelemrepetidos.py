def contar_elementos(tupla):
    contador = {}
    for elemento in tupla:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

if __name__ == "__main__":
    tupla = (1, 2, 3, 1, 2, 3, 1, 2, 3)
    resultado = contar_elementos(tupla)
    print("Conteo de elementos en la tupla:", resultado)
