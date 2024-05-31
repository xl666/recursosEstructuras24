class Ruta:
    def __init__(self, ruta):
        partes = ruta.split('/',)
        self.directorio = '/'.join(partes[:-1]) + '/' if len(partes) > 1 else './'
        self.archivo = partes[-1]
        self.nombre_base, self.extension = self.archivo.rsplit('.', 1) if '.' in self.archivo else (self.archivo, '')
    def __repr__(self):
        return f'directorio:{self.directorio}:archivo:{self.archivo}:extension:{self.extension}'


if __name__ == '__main__':
    rutita = input()
    print(Ruta(rutita))