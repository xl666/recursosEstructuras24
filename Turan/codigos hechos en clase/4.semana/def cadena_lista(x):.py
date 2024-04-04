def cadena_lista(x):
    lista=[]
    for i in range(x):
        #print(f"Entre los datos del alumno {i+1}")
        cadena=str(input(""))
        aux = cadena.split(" ")
        lista.append((aux[-1].strip("()")))
    print("\n".join(lista))
       
if __name__ == '__main__':
        cantidad = int(input())
        cadena_lista(cantidad)