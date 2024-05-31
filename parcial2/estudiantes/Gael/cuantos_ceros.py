def cuantos_ceros_rec(binaria,contador):
    if not binaria:
        return contador
    frente=binaria[0]
    resto=binaria[1:]
    if frente=='0':
        contador+=1
    return cuantos_ceros_rec(resto,contador)

def cuantos_ceros(binaria):
    return cuantos_ceros_rec(binaria,0)

if __name__=='__main__':
    cadena_binaria=input()
    print(cuantos_ceros(cadena_binaria))