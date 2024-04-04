def cifrado_cesar(shift, cadena):
    resultado = ""
    for caracter in cadena:
        if caracter.isalpha():
            nuevo_indice = (ord(caracter) - ord('a') + shift) % 26
            resultado += chr(ord('a') + nuevo_indice)
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    shift = int(input())
    cadena_sin_cifrar = input()

    cadena_cifrada = cifrado_cesar(shift, cadena_sin_cifrar)
    print(cadena_cifrada)
