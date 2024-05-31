
def recuperar_info(info: str) -> tuple:
    """
    Procesa una línea de información de usuario
    de acuerdo al formato de shadow,
    regresa el nombre de usuario
    y un diccionario con los campos.

    info: str
    returns: usuario, dict, diccionario de campos
    """
    partes = info.split(':')
   
    usuario = partes[0]
    resto = partes[1]
    campos = resto.split('$')
    dict_campos = {}
    dict_campos['algoritmo'] = campos[1]
    dict_campos['salt'] = campos[2]
    dict_campos['password'] = campos[3]
    return usuario, dict_campos
    

def construir_diccionario(cadenas: list) -> dict:
    """
    Construye un diccionario de diccionarios
    con la información de las cadenas
    las ladenas usan el formato del archivo
    shadow.

    cadenas: list
    returns: dict 
    """
    res = {}
    for info in cadenas:
        usuario, dict_info = recuperar_info(info)
        res[usuario] = dict_info
    return res


if __name__ == '__main__':
    n_usuarios = int(input())
    usuario = input()
    campo = input()
    cadenas = []
    for _ in range(n_usuarios):
        cadenas.append(input())
    informacion = construir_diccionario(cadenas)
    print(informacion[usuario][campo])
