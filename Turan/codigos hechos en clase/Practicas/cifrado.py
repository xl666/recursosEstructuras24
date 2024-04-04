def cifrado(cadena,shift):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x', 'y','z']
    coded = []
    for x in cadena:
        if x == ' ':
            coded.append(' ')
        else:
            yer = int(abc.index(x))
            coded.append(abc[(yer + shift) % 26])
    cadena_cifrado =''.join(coded)
    return cadena_cifrado

if __name__=='__main__':
    cadena = str(input())
    shift = int(input())
    if shift > 0:
        cadena_cifrado = cifrado(cadena,shift)
        print(cadena_cifrado)
    else:
        print(cadena)
    