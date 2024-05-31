def es_palindromo(palabra: str) -> bool:
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def maximo_lista(lista: list) -> int:
    if len(lista) == 1:
        return lista[0]
    max_del_resto = maximo_lista(lista[1:])
    return lista[0] if lista[0] > max_del_resto else max_del_resto

def combinaciones(conjunto: str) -> list:
    if len(conjunto) == 0:
        return [""]
    primer_caracter = conjunto[0]
    resto_combinaciones = combinaciones(conjunto[1:])
    resultado = []
    for combinacion in resto_combinaciones:
        resultado.append(combinacion)
        resultado.append(primer_caracter + combinacion)
    return resultado

def longitud_cadena(cadena: str) -> int:
    if cadena == "":
        return 0
    return 1 + longitud_cadena(cadena[1:])


print(longitud_cadena("Hola Mundo"))  # Output: 10
print(combinaciones("abc"))
print(maximo_lista([1, 5, 3, 9, 2]))  # Output: 9
print(potencia(2, 3))  # Output: 8
print(potencia(5, 0))  # Output: 1
print(es_palindromo("radar"))  # Output: True
print(es_palindromo("hello"))  # Output: False