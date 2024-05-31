def reversa(cadena):
    if not cadena:
        return ''
    res = ''
    for i in range(1, len(cadena) + 1):
        res += cadena[-i]
    return res

def es_palindromo(cadena):
    cadena_sin_espacios = cadena.replace(" ", "")  # Eliminar espacios
    reverso = reversa(cadena_sin_espacios)
    return cadena_sin_espacios == reverso

def main():
    entrada = input()
    resultado = es_palindromo(entrada)
    print(resultado)

if __name__ == "__main__":
    main()