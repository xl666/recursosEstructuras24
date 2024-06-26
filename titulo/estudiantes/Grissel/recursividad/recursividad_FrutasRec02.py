def frutas(indice: int, final: int, lista: list)-> list:
    fruta = input() # ---> ingresa la fruta
    # ---> si el indice actual es menor que el indice final, se realiza:
    if indice < final:
        # ---> si la fruta ingresada es una de las frutas rojas['cereza', 'manzana', 'ciruela']
        if fruta == "cereza" or fruta == "manzana" or fruta == "ciruela":
            # ---> si esta fruta en lista, llamar la función con el indice incrementado
            if fruta in lista:
                frutas(indice+1, final, lista)
            else:
                # ---> si fruta no esta en lista, se añade y se llama la funcion con el indice incrementado
                lista.append(fruta)
                frutas(indice+1, final, lista)
        else:
            # ---> si fruta ingresada no es ninguna de las frutas, se llama la funcion con indice incrementado
            frutas(indice+1, final, lista)
    return lista # ---> como indice no es menor que el indice final, se retorna la lista

if __name__ == "main":
    index = int(input())
    frutas_rojas = frutas(1, index, [])
    print(frutas_rojas)