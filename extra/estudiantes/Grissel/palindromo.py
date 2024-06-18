# Recorrido inverso de la cadena
cadena = input()
for i in range(len(cadena)-1, -1, -1):
    reverso = cadena[i]
    if reverso == cadena:
        print('True')
    else: ('False')