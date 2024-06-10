def leerDic(info: list) -> dict:
    """
    En esta función se hace una separación de cada uno de los usuarios
    proporcionados junto con su respectivas contraseñas y se crea un diccinario
    para usarlo en la siguiente funcion
    """
    lista = []
    llaves = []
    valores = []
    for i in range(len(info)):
        lista.append(info[i].split(':'))
        
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if j % 2 == 0:
                llaves.append(lista[i][j])
            else:
                valores.append(lista[i][j])
    var = tuple(zip(llaves, valores))
    diccionario = {}
    for llave, valor in var:
        diccionario[llave] = valor

    return diccionario

def crearDic(dic: dict) -> dict:
    """
    En esta funcion se separan cada uno de las contraseñas y 
    y se guardan en otro diccionario para que sea el subdiccionario 
    en donde se encuentran ordenados por categorías y se retorna este nuevo
    diccionario con nuevos valores
    """
    llaves2 = ['algoritmo', 'salt', 'password']
    diccionario_final = {}
    
    for usuario, valor in dic.items():
        valores2 = valor.split('$')
        subdic = {}
        for i in range(1, len(valores2)):
            subdic[llaves2[i - 1]] = valores2[i]
        diccionario_final[usuario] = subdic
    
    return diccionario_final

def campoEn(usuario: str, campo: str, dicFin: dict) -> str:
    """
    En esta funcion se comprueba que el usuario y el campo que se solicito esta
    en el diccionario y se imprime dicho campo
    """
    if usuario in dicFin:
        subusuario = dicFin[usuario]
        if campo in subusuario:
            return subusuario[campo] 

if __name__ == '__main__':
    n = int(input())
    usuario = input()
    campo = input()
    info = []

    for _ in range(n):
        info.append(input())
    copia = info.copy()
    dic = leerDic(copia)
    dicFin = crearDic(dic)
    print(campoEn(usuario, campo, dicFin))
