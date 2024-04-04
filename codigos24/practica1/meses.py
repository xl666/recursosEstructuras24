
mes = int(input())

def regresar_mes(mes):
    lista_meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    return lista_meses[mes - 1]

def regresar_mes2(mes):
    diccionario_meses = {1: 'enero', 2: 'febrero'}
    return diccionario_meses[mes]

print(regresar_mes(mes))

