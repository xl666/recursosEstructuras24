class RutaUnix():
    def __init__(self,directorio,archivo,extension):
        self.directorio='/'.join(directorio)
        self.archivo=archivo
        self.extension=extension[-1]
    
        
    def __repr__(self):
        if len(directorio)>1:
            return 'directorio:%s/:archivo:%s:extension:%s'%(self.directorio, self.archivo,self.extension)
        return 'directorio:./:archivo:%s:extension:%s'%(self.archivo,self.extension)
    
if __name__ == '__main__':
    entrada=input()
    partes=entrada.split('/')
    directorio=partes[0:-1]
    archivo=partes[-1]
    extension=archivo.split('.')
    print(RutaUnix(directorio,archivo,extension))