mes = int(input())


def regresar_mes(mes):
    lista_meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                   'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    return lista_meses[mes - 1]


regresar_mes(mes)
