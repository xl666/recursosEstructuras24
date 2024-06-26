def quita_repetidas(lista):
    lista_nueva=[]
    for _ in lista:
        if _ not in lista_nueva:
            lista_nueva.append(_)
    return lista_nueva

def buscar_frutas_rojas_rec(lista, nueva_lista, frutas_rojas):
    if lista:
        if lista[0] in frutas_rojas:
            nueva_lista.append(lista[0])
        lista.pop(0)
        #print('lista_original: ', lista)
        #print('lista_nueva: ',nueva_lista)
        nueva_lista = buscar_frutas_rojas_rec(lista, nueva_lista, frutas_rojas)
    return nueva_lista 

if __name__ == '__main__':
    frutas_rojas = ['cereza', 'ciruela', 'manzana']
    n = int(input())
    lista_frutas = [input() for _ in range(n)]
    lista_sin_repetidos = quita_repetidas(lista_frutas)
    print(buscar_frutas_rojas_rec(lista_sin_repetidos, [], frutas_rojas))    