def contar_puntos(cadena):
    cadena_limpia = cadena.strip()
    num_puntos = 0
    punto_anterior = False
    
    for caracter in cadena_limpia:
        if caracter == '.' and not punto_anterior:
            num_puntos += 1
            punto_anterior = True
        elif caracter != '.':
            punto_anterior = False
    return num_puntos

if __name__ == '__main__':
    entrada = input()
    resultado = contar_puntos(entrada)
    print(resultado)
    
