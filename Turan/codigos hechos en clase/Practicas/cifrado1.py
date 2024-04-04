def cifrado(cadena,shift):
    abc = 'abcdefghijklmnoprqstuvwxyz'
    coded = ''
    for x in cadena:
        if x == " ":
            coded += " "
        else:
            i = (abc.find(x) + shift)  % 26
            coded += abc[i]
    return coded







if __name__== '__main__':
    cadena_original = str(input())
    shift = int(input())
    print(cifrado(cadena_original, shift))