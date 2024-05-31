class Ruta:
    def __init__(self, ruta):
        if '/' in ruta:
            partes = ruta.rsplit('/', 1)
            self.directorio = partes[0] + '/'
            self.archivo = partes[1]
        else:
            self.directorio = './'
            self.archivo = ruta
        self.extension = self.archivo.split('.')[-1]

    def __repr__(self):
        return f"directorio:{self.directorio}:archivo:{self.archivo}:extension:{self.extension}"


if __name__ == '__main__':
    entrada = input()
    ruta = Ruta(entrada)
    print(ruta)
