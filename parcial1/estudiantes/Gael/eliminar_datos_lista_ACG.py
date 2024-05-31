def lista_eliminado (n_elem, elem_eliminar):
    aux=[int(input()) for n in range (n_elem)]
    res=[n for n in aux if n != elem_eliminar]
    return res

if __name__=='__main__':
    elem_eliminar=int(input())
    n_elem=int(input())
    print (lista_eliminado(n_elem,elem_eliminar))