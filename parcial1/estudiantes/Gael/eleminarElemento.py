def quitar_elemento(elemento,lista):
    return [x for x in lista if x!= elemento]

def  quitar_elemento2(elemento,lista):
    res=[]
    for x in lista:
        if x!= elemento:
            res.append(x)
    return res
if __name__=='__main__':#No hacerlos más complejos de lo necesario en el examen
    v=int(input())
    n=int(input())
    lista = [int(input) for _ in range(n)]
    print(quitar_elemento(v,lista))
