

def generar_sucesores(estado: tuple) -> list:
    """
    Determina los estados hijos que se
    pueden generar a partir del estado
    de entrada

    estado = (5, 3)
    
    """
    jarra_5, jarra_3 = estado

    sucesores = []
    
    # Llenar jarra de 5 litros
    if jarra_5 != 5:
        sucesores.append((5, jarra_3))

    # Llenar jarra de 3 litros
    if jarra_3 != 3:
        sucesores.append((jarra_5, 3))

    # Vaciar jarra de 5 litros
    if jarra_5 != 0:
        sucesores.append((0, jarra_3))

    # Vaciar jarra de 3 litros
    if jarra_3 != 0:
        sucesores.append((jarra_5, 0))

    # Pasar de la de 5 a la de 3
    if jarra_3 != 3 and jarra_5 != 0:
        espacio_en_tres = 3 - jarra_3
        nuevo_5 = jarra_5 - espacio_en_tres
        if espacio_en_tres < jarra_5:
            nuevo_3 = 3
        else:
            nuevo_3 = jarra_3 + jarra_5
        sucesores.append((nuevo_5, nuevo_3))

    # Pasar de la de 3 a la de 5
    if jarra_5 != 5 and jarra_3 != 0:
        espacio_en_cinco = 5 - jarra_5
        nuevo_3 = jarra_3 - espacio_en_cinco
        if espacio_en_cinco < jarra_3:
            nuevo_5 = 5
        else:
            nuevo_5 = jarra_5 + jarra_3
        sucesores.append((nuevo_5, nuevo_3))


    return sucesores

def es_meta(estado):
    jarra_5, jarra3 = estado
    if jarra_5 == 4:
        return True
    return False

def buscar_profundidad_rec(estado: tuple, visitados: list, resultado: list) -> None:
    """
    Resuelve el problema de las jarras en profundidad.

    estado: tuple, visitados
    returns: tuple
    """
    if es_meta(estado):        
        resultado[0] = visitados + estado
        return 

    sucesores = generar_sucesores(estado)
    print(sucesores)
    for sucesor in sucesores:
        if not sucesor in visitados and not resultado:            
            return buscar_profundidad_rec(sucesor, visitados + [estado], resultado)
    

def buscar_profundidad():
    res = []
    buscar_profundidad_rec((0,0), [], res)
    return res[0]
