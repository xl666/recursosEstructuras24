class Ruta():
    def __init__(self,ruta):
        partes=ruta.split('/')
        if not '/' in ruta:
            self.directorio='./'
        else:
            self.directorio='/'.join(partes[:-1])+'/'
        self.archivo=partes[-1]
        self.extension=self.archivo.split('.')[-1]
    def __repr__(self):
        plantilla='directorio:%s:archivo:%s:extension:%s'
        return plantilla %(self.directorio,
                           self.archivo,
                           self.extension)

if __name__=='__main__':
    ruta=input()
    objeto=Ruta(ruta)
    print(objeto)