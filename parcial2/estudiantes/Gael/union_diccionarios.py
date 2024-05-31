def llenar_diccionarios(longitud:int)->dict:
    """
    Crea un diccionario y lo llena según la longitud determinada
    longitud: numero entero que representa el número de llaves y valores
    que tendrá el diccionario
    return: dict
    """
    res={}
    for _ in range(longitud):
       llave=input()
       valor=int(input())
       res[llave]= valor
    return res
    
def unir_diccionarios(diccionario1:dict, diccionario2:dict)->dict:
    """
    une 2 diccionarios, si tienen una llave en común, suma el valor que tiene la llave
    en ambos diccionarios
    return: dict
    """
    res={}
    for llave in diccionario1.keys():
        res[llave]=diccionario1[llave]
    
    for llave2 in diccionario2.keys():
        if not llave2 in res.keys():
             res[llave2]=diccionario2[llave2]
        else:
            res[llave2]+=diccionario2[llave2]
    return res

def imprimir_diccionario(diccionario:dict)->None:
    """
    Imprime el resultado como lo espera el sistema
    diccionario: dict
    returns: None
    """
    llaves_ordenadas=sorted(diccionario.keys())
    for llave in llaves_ordenadas:
        print('%s: %s'%(llave,diccionario[llave]))

if __name__=='__main__':
    longitud1=int(input())
    longitud2=int(input())
    diccionario1=llenar_diccionarios(longitud1)
    diccionario2=llenar_diccionarios(longitud2)
    imprimir_diccionario(unir_diccionarios(diccionario1, diccionario2))