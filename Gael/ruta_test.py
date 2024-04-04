import ruta_objeto
ob1=ruta_objeto.Ruta('/tmp/nuevo_directorio/archivo.txt')
assert ob1.__repr__()=='directorio:tmp/nuevo_directorio/:archivo:archivo.txt:extension:txt'
print('todo ok')
ob2=ruta_objeto.Ruta('hola.com.txt')
assert ob2.__repr__()=='directorio:./:archivo:hola.com.txt'