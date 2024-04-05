# Dada una cadena de entrada, determina cuántos caracteres "." tiene
#Considera que si los puntos están seguidos sólo se cuentan una vez,
#esto es, no se cuentan repeticiones seguidas
def contarpuntos(cadena):
    contador = 0
    prev_char = None

    for char in cadena:
        if char == "." and char != prev_char:
            contador += 1
        prev_char = char

    return contador

if __name__ == "__main__":
    cadena = input()
    cantidaddepuntos = contarpuntos(cadena)
    print(cantidaddepuntos)