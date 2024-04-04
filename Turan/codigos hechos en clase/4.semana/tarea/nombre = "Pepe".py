def formato(cadena):
    aux = cadena.split('.')
    nombre= aux[0]
    edad= int(aux[1])
    grado= aux[2]
    cadena= "<nombre>%s</nombre><edad>%d</edad><grado>%s</grado>" % (nombre, edad, grado)
    return cadena


cadena = 'Pepe Pecas.15.primaria'
print(formato(cadena))




