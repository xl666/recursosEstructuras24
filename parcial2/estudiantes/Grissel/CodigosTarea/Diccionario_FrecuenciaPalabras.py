def frecuenciaPalabras():
    diccionario = {}
    for palabras in partes:
        if palabras in diccionario:
            diccionario[palabras] += 1
        else:
            diccionario[palabras] = 1
    ordenada = sorted(diccionario.keys())
    for palabras in ordenada:
        print(f"{palabras}: {diccionario[palabras]}")


if __name__ == '__main__':
    cadena = input()
    partes = cadena.split(' ')
    frecuenciaPalabras()