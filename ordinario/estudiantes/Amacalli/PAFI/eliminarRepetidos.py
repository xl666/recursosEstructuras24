def eliminar (frase):
    long = len(frase)
    i = 0
    caracteres = ''

    while i < long:
        caracteres += frase[i]
        if not frase[i].isalnum():
            while i < long - 1  and frase[i] == frase[i + 1]:
                i += 1
        i += 1
    return caracteres
#oalonso@uv.mx
if __name__ == '__main__':
    frase = input()
    print(eliminar(frase))