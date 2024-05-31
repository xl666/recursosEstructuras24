def llenar_lista(longitud):
    res=[]
    for _ in range(longitud):
        res.append(int(input()))
    return res
def repetida(lista):
    res=[]
    for i in range(len(lista)):
        aux=0
        for j in range(len(lista)):
            if lista[i]==lista[j]:
                aux+=1
        if aux>1:
            res.append(1)
        else:
            res.append(0)
    for elem in res:
        if elem==0:
            return False
    return True
            
if __name__=='__main__':
    longitud=int(input())
    print(repetida(llenar_lista(longitud)))