# Paso 1: Crear una lista
# Paso 2: Ingresar el numero para revisar si pertenece a nuestra lista
# Paso 3: Ingresar el numero n (int) de elementos de mi lista
# Paso 4: ingresar n elementos de la lista
# Paso 5: Revisar si mi numero pertenece a la lista
# Paso 6: Regresar True si pertenece, Regresar False si no

def pertenece_recursivo(lista: list, n_elemento: int, i: int) -> bool:
    """
    Regresa True o False si n_elemento pertenece a la lista

    """
    if i >= len(lista): # CASO BASE 1: n_elemento no se encontró en mi lista
        return False
    else:
        if n_elemento == lista[i]: # CASO BASE 2: n_elemento si se encontró en la lista
            return True
    
    return pertenece_recursivo(lista, n_elemento, i + 1)

if __name__ == '__main__':
    n = int(input())
    n_elemento = int(input())
    lista = [int(input()) for _ in range(n_elemento)]
    print(pertenece_recursivo(lista, n, 0))