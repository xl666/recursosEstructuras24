def puntos_continuos(cadena):
    contador = 0
    punto_anterior = False

    for caracter in cadena:
        if caracter == '.':
            if not punto_anterior:
                contador += 1
            punto_anterior = True
        else:
            punto_anterior = False

    return contador

if __name__ == '__main__':
    cadena = input()
    resultado = puntos_continuos(cadena)
    print(resultado)  
