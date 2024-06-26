def crear_diccionario(n):
    diccionario = {}
    for _ in range(n):
        llave, valor = input().split(':') # ---> dividir entrada en llave y valor
        
        if valor == 'OK':
            if llave not in diccionario: # ---> si no hay llave inicializar contador 
                diccionario[llave] = 0 # ---> contador de 'OK' comienza en 0
            diccionario[llave] += 1 # ---> contar los 'OK' cada vez que se encuentre uno
            
    return diccionario
        
def dominios_OK(diccionario):
    lista_OK = []
    for dominio, valores in diccionario.items(): # --> explicame esto tambien
        if valores >= 2: # ---> si valores 'OK' son mayores o igual a 2 agregamos a la lista
            lista_OK.append(dominio)
    return lista_OK

if __name__ == '__main__':
    n = int(input())
    diccionario = crear_diccionario(n) # ---> crear diccionario con las entradas
    dominios = dominios_OK(diccionario) # ---> obtener los dominios con al menos dos 'OK'
    # dominios_ordenados = sorted(dominios)
    dominios.sort()
    for dominio in dominios:
        print(dominio)
        