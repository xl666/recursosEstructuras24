def par_imn(g):
    pares=[]
    impares=[]
    for numeros in g:
        if (numeros%2)==0:
            pares.append(numeros)
        else:
            impares.append(numeros)
    return(pares,impares)


a=int(input())
g=[]
if (a>0) or (a==0):
    if (a%2==0):
        for i in range (a):
            g.append(i)
        g.append(a)
        pares, impares=par_imn(g)
        print(sum(impares))
    else:
        for i in range (a):
            g.append(i)
        g.append(a)
        pares, impares=par_imn(g)
        print(sum(impares))
