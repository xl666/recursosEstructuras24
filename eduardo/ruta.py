class RutaUnix:
    def __init__(self, ruta):
        partes = ruta.rsplit('/', 1)
        if len(partes) == 1:  # Si no hay directorio en la ruta
            self.directorio = './'
            self.archivo = partes[0]
        else:
            self.directorio = partes[0] + '/'
            self.archivo = partes[1]
        self.extension = self.archivo.split('.')[-1]

    def __repr__(self):
        return f"directorio:{self.directorio}:archivo:{self.archivo}:extension:{self.extension}"


def obtener_ruta():
    ruta = input()
    return RutaUnix(ruta)

objeto_ruta = obtener_ruta()
print(objeto_ruta)