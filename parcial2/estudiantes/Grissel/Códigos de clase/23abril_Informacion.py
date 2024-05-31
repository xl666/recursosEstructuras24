def recuperar_info(info: str) -> tuple:
    """
    Procesa una línea de informacion de usuario
    de acuerdo al formato shadow, regresa
    un diccionario con los campos.
    info: str
    return: dict, diccionario de campo
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

def contruir_diccionario(cadenas: list) -> dict:
    """
    Construye un diccionario de diccionarios con la información
    de las cadenas usan el formato del archivo shadow
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
    informacion = contruir_diccionario(cadenas)
    print(informacion[usuario][campo])