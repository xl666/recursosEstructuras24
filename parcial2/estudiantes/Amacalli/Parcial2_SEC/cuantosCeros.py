def contar_recursivo(cadena: str, cont: int) -> int:
    """
    Cuenta cuantos ceros hay en la cadena binaria
    """
    if not cadena:
        return cont
    
    frente = cadena[0]
    resto = cadena[1:]

    if frente == '0':
        cont = cont + 1
    
    return contar_recursivo(resto, cont)

def contar(cadena: str) -> int:
    return contar_recursivo(cadena, 0)

if __name__ == '__main__':
    cadena = input()
    print(contar(cadena))