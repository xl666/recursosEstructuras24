def eliminarElementos(v_valoreliminado, n_numelem, lista):
    nueva_lista = [num for num in lista if num != v_valoreliminado]
    print(nueva_lista)

if __name__ == "__main__":
    v_valoreliminado = int(input())
    n_numelem = int(input())
    lista = [int(input())for _ in range (n_numelem)]
    eliminarElementos(v_valoreliminado, n_numelem, lista)




