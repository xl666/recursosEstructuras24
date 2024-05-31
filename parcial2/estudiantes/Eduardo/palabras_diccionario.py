if __name__ == "__main__":
    frase = input()

    separado = frase.split(" ")
    diccionario = {}

    for i in separado:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1

    ordenado = dict(sorted(diccionario.items()))
    
    formateo = ""
    for _ in ordenado:
        formateo += "{}: {}\n".format(_, ordenado[_])

    print(formateo)