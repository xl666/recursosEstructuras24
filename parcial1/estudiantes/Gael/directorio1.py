
class Ruta:
    def __init__(self, ruta):
        if '/' in ruta:
            self.directorio, self.archivo = ruta.rsplit('/', 1)
            self.directorio += '/'
        else:
            self.directorio = './'
            self.archivo = ruta
        self.extension = self.archivo.split('.')[-1]

    def __repr__(self):
        return f'directorio:{self.directorio}:archivo:{self.archivo}:extension:{self.extension}'

ruta = input()
objeto_ruta = Ruta(ruta)
print(objeto_ruta)
