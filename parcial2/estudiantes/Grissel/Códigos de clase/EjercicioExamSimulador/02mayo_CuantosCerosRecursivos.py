# casos base:
#   lista vacía

# casos recursivos
#   1. lista no está vacía
#       Revisar si en el frente = 0
#           si: contarlo
#           No: dejarlo pasar


# ---> SI es a la cola ver que variables me sirven
def cuantos_ceros2_rec(cadena: str, acumulador: int) -> int:
    if not cadena:
        return acumulador
    frente = cadena[0]
    resto = cadena[1:]
    if frente == '0':
        return cuantos_ceros2_rec(resto, acumulador + 1)
    else:
        return cuantos_ceros2_rec(resto, acumulador)

# ----> si no es ala cola no variables extras
def cuantos_ceros_rec(cadena: str) -> int:
    """
    Cuenta los elementos dentro de la cadena
    cadena: str
    acumulador: int
    returns: int
    """
    if not cadena:
        return 0
    frente = cadena[0]
    resto = cadena[1:]
    if frente == '0':
        return 1 + cuantos_ceros_rec(resto)
    else:
        return cuantos_ceros_rec(resto)
    
if __name__ == '__main__':
    cadena = input()
    # print(cuantos_ceros_rec(cadena))
    print(cuantos_ceros2_rec(cadena))

# -- no temas conceptos avanzados de funciones
# -- procesamiento de archivos mo viene examen datos

# estructuras asociativas si
# recursividad si 
# diccionario
# arboles
# recursividad