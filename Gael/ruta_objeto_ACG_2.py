class RutaUnix():
    def __init__(self,ruta):
        if not '/' in ruta:
            self.directorio='./'
        else:
            self.partes=ruta.split('/')[0:-1]
            self.directorio='/'.join(self.partes)
            self.directorio+='/'
        self.archivo=ruta.split('/')[-1]
        self.extension=self.archivo.split('.')[-1]
        
    def __repr__(self):
        return 'directorio:%s:archivo:%s:extension:%s'%(self.directorio, self.archivo,self.extension)
        
    
if __name__ == '__main__':
    ruta=input()
    objeto_resultado=RutaUnix(ruta)
    print(objeto_resultado)

 