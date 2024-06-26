if __name__ == '__main__':
    diccionario = {}
    n = int(input())
    for _ in range(n):
        # ---> Dividir la entrada en llave y valor
        llave, valor = input().split(':')
        # ---> si llave no esta en diccionario, inicializar una lista vacia para esa llave
        if llave not in diccionario:
            diccionario[llave] = []
        
        diccionario[llave].append(valor) # ---> añadir valor a la lista correspondiente a la llave
    
    m = int(input())
    for _ in range(m):
        consulta = input()
        if consulta in diccionario:
            for valor in diccionario[consulta]:
                print(valor)
        else:
            None
            
#if __name__ == '__main__':
#   diccionario = {}
 #  n = int(input())
   # for _ in range(n):
    #    llave, valor = input().split(':')
     #   diccionario[llave[0]] = [valor[1]]    
    
#    m = int(input())
#    for _ in range(m):
#        consulta = input()
#        print(diccionario[consulta])  