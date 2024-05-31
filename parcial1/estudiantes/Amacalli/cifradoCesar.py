import string

def cifrado(desplazamiento, cadena):
    alfabeto = string.ascii_lowercase
    codificacion = ''
    for caracter in cadena:
        if caracter != ' ':
            indice = alfabeto.index(caracter)
            shift = (indice + desplazamiento) % 26
            cesar = alfabeto[shift]
            codificacion += cesar
        else:
            codificacion += caracter
    return codificacion
    

if __name__ == '__main__':
    desplazamiento = int(input())
    texto = input()
    print(cifrado(desplazamiento, texto))