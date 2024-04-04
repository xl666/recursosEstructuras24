import ruta


ob1 = ruta.Ruta('/tmp/nuevo_directorio/archivo.txt')
assert ob1.__repr__() == 'directorio:/tmp/nuevo_directorio/:archivo:archivo.txt:extension:txt'

ob2 = ruta.Ruta('hola.com.txt')
assert ob2.__repr__() == 'directorio:./:archivo:hola.com.txt:extension:txt'

print('Todo OK')
