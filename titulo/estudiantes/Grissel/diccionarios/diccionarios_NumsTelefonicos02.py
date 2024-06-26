def diccionario_personas(diccionario, n):
    for _ in range(n):
        llave_valor = input().split(':')
        diccionario[llave_valor[0]] = llave_valor[1]
    return llave_valor[1]

if __name__ == '__main__':
    diccionario = {}
    n = int(input()) 
    res = diccionario_personas(diccionario, n)
    m = int(input())
    for _ in range(m):
        consulta = input()
        print(diccionario[consulta])
#    print(diccionario['pepe'] + diccionario['pancho'])
#    if diccionario['pepe'] == '22-83-23-23':
#        print(True)
#    else:
#        print(False)