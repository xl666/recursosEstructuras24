def cifrado_cesar(shift, cadena):
    cifrada = ""
    for caracter in cadena:
        if caracter.isalpha():
            nueva_posicion = ord(caracter) + shift
            if caracter.islower():
                if nueva_posicion > ord('z'):
                    nueva_posicion -= 26
            cifrada += chr(nueva_posicion)
        else:
            cifrada += caracter
    return cifrada


shift = int(input())
cadena = input()
print(cifrado_cesar(shift, cadena))
