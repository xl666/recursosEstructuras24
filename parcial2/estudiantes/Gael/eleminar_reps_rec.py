def eliminar_duplicados(lista:list, resultado:list)->list:
    if not lista:
        return resultado
    frente=lista[0]
    resto=lista[1:]
    if not frente in resultado:
        resultado.append(frente)
    return eliminar_duplicados(resto,resultado)

if __name__=='__main__':
    elem_lista=int(input())
    l=[int(input()) for i in range(elem_lista)]
    resultado=[]
    print(eliminar_duplicados(l,resultado))
