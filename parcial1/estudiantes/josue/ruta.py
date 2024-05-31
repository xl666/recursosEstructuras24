class Ruta():
    def __init__(self, ruta):
        partes = ruta.rsplit('/', 1)
        if len(partes) == 1: 
            self.directorio = './'
            self.archivo = partes[0]
        else:
            self.directorio = partes[0] + '/'
            self.archivo = partes[1]
            partes_archivo = self.archivo.rsplit('.', 1)
            self.extension = partes_archivo[1]

    def __repr__(self):
        return f"directorio:{self.directorio}:archivo:{self.archivo}:extension:{self.extension}"


if __name__ == '__main__':
    entrada = input()

    objeto_ruta = Ruta(entrada)

    print(objeto_ruta)
