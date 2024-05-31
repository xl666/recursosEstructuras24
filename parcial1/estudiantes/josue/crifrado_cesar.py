def cifrado_cesar(shift, cadena):
    resultado = ""

    for caracter in cadena:
        if 'a' <= caracter <= 'z': 
            indice = (ord(caracter) - ord('a') + shift) % 26
            nuevo_caracter = chr(ord('a') + indice)
        else:
            nuevo_caracter = caracter

        resultado += nuevo_caracter

    return resultado


shift = int(input())
cadena_sin_cifrar = input()

cadena_cifrada = cifrado_cesar(shift, cadena_sin_cifrar)


print(cadena_cifrada)
