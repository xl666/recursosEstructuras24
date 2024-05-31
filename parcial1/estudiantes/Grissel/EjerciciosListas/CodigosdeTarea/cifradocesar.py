def cifradoCesar(shift, cadena):
    cadena_cifrada = ""
    espacios = 0  
    for caracter in cadena:
        if caracter == " ":
            cadena_cifrada += " "
            espacios += 1  
            continue
        codigo = ord(caracter) - ord('a')
        caracter_cifrado = chr((codigo + shift) % 26 + ord('a'))
        cadena_cifrada += caracter_cifrado
    cadena_cifrada += " " * espacios
    return cadena_cifrada

if __name__ == '__main__':
    shift = int(input())
    cadena = input()
    cadena_cifrada = cifradoCesar(shift, cadena)
    print(cadena_cifrada)