def letraMayuscula(palabra, vocal):
    nueva = ''

    for letra in palabra:
        if letra == vocal:
            nueva += letra.capitalize()
        else:
            nueva += letra
    return nueva

if __name__ == '__main__':
    palabra = input('Ingresa una palabra: ')
    vocal = input('Ingresa la vocal que quieres que se ponga en mayusculas: ')
    print(letraMayuscula(palabra, vocal))
    