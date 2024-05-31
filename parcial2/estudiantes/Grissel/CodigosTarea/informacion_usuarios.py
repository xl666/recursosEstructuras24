def solicitar_cadenas(n):
    """
    Solicita cadenas en un diccionario con formato llave-valor.
    Regresa un diccionario con las llaves y valores proporcionados.
    """
    diccionario = {}
    for _ in range(n):
        cadena = input()
        cadena_guardada = cadena.split(':')
        llave = cadena_guardada[0]
        valor = cadena_guardada[1]
        diccionario[llave] = valor
    return diccionario   

def campo(usuario, campo, diccionario):
    """
    Dependiendo de la opción del campo (algoritmo, salt, password),
    imprime el valor que corresponda a la clave especificada por el usuario.
    """
    if usuario in diccionario:
        cadena = diccionario[usuario]
    else:
        print('Usuario no encontrado')
        cadena = None

    if cadena:
        partes = cadena.split('$')
        if campo == 'algoritmo':
            print(partes[1])
        elif campo == 'salt':
            print(partes[2])
        elif campo == 'password':
            print(partes[3])
        else:
            print('Opción no válida')
    else:
        print('Usuario no encontrado')

if __name__ == '__main__':
    n = int(input())
    usuario = input()
    campo_de_interes = input()
    diccionario = solicitar_cadenas(n)
    campo(usuario, campo_de_interes, diccionario) 