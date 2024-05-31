def burbuja (lista):
    k=0#para que deje de recorres los último elementos, por cada ciclo se van ordenando los últimos elementos
    for i in range(len(lista)-1):
        n=0
        for j in range(len(lista)-k):
            print(j)
            aux=lista[j]
            if n<(len(lista)-1):
                if lista[j]>lista[j+1]:
                    aux=lista[j+1]
                    lista[j+1]=lista[j]
                    lista[j]=aux
            n+=1
        k+=1
    return lista

if __name__=='__main__':
    longitud=int(input())
    lista=[int(input()) for _ in range (longitud)]
    print(burbuja(lista))