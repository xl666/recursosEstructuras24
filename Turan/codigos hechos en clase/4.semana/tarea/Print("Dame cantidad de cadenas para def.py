

def cadena(x):
    lista=[]
    for i in range(x):
        cadena=str(input(''))
        lista.append(cadena)
        print (lista)
    nuevalista = lista.join()
    print(nuevalista)


print("Dame cantidad de cadenas para definir")
cantidad=int(input())
cadena(cantidad)