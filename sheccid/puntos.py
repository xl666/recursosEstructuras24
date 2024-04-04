def contar_puntos_no_continuos(cadena):
    puntos_contados = 0
    punto_anterior = False

    for caracter in cadena:
        if caracter == ".":
            if not punto_anterior:
                puntos_contados += 1
            punto_anterior = True
        else:
            punto_anterior = False

    return puntos_contados

def main():
    entrada = input()
    resultado = contar_puntos_no_continuos(entrada)
    print(resultado)

if __name__ == "__main__":
    main()
