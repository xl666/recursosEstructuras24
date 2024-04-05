def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y quitar los espacios
    cadena = cadena.lower().replace(" ", "")

    # Comparar la cadena con su reverso
    return cadena == cadena[::-1]


cadena = input()
print(es_palindromo(cadena))
