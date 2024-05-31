def pertenece_recursivo(lista: list, n_elemento: int, i: int) -> bool:
    """
    Regresa True o False si n_elemento pertenece a la lista.
    """
    # Caso base: si i es igual o mayor a la longitud de la lista, retornar False
    if i >= len(lista):
        return False
    
    # Caso base: si n_elemento es igual al elemento de lista[i], retornar True
    if n_elemento == lista[i]:
        return True
    
    # Llamada recursiva: avanzar en el índice
    return pertenece_recursivo(lista, n_elemento, i + 1)

if __name__ == '__main__':
    n = int(input())  # Valor a buscar (55)
    n_elemento = int(input())  # Número de elementos en la lista (4)
    # Lista con n_elemento valores
    lista = [int(input()) for _ in range(n_elemento)]
    # Iniciar la búsqueda desde el primer índice (0)
    print(pertenece_recursivo(lista, n, 0))
