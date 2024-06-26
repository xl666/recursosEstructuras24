d1 = {'amazon.com':'OK',
      'uv.mx':'OK',
      'google.com':'ERROR',
      'amazon.com':'OK',
      'google.com':'ERROR'}

# modificar elemento - - - - - - - - - - - - - - - - - - - - - - 
#d1['Nombre'] = 'Laura'

# crear key que no exista - - - - - - - - - - - - - - - - - - - -
# d1['Direccion'] = 'Calle 123'

#imprimir key - - - - - - - - - - - - - - - - - - - - - - - - - -
for x in d1:
      if d1[x]:
            print(x)

# imprimir value - - - - - - - - - - - - - - - - - - - - - - - -
# for x in d1:
# print(d1[x])

# imprime key y value - - - - - - - - - - - - - - - - - - - - - -
# for x, y in d1.items():
# print(x, y)

#amazon.com:OK
# uv.mx:OK
# google.com:ERROR
# amazon.com:OK
# google.com:ERROR