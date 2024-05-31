# Considera una cadena que representa una ruta al estilo Unix:
#/tmp/nuevo_directorio/archivo.txt

#Crea una clase con las siguientes propiedades (se dan valores de ejemplo):
#- directorio: /tmp/nuevo_directorio/  (notar que se deja diagonal al final)
#- archivo: archivo.txt
#- extension: txt

#Una ruta válida puede ser sólo el nombre del archivo, sin ruta de directorio,
#en cuyo caso el directorio es el directorio actual (./). Por ejemplo para esta ruta:

#pinguino.com.png

#Las propiedades serían las siguientes
#- directorio: ./
#- archivo: pinguino.com.png
#- extension: png

#Notar que en el nombre de archivo (y nombres de directorios) 
#puede haber varios puntos, pero el sistema siempre pasará archivos 
#con alguna extensión.

#Tu trabajo consiste en crear la clase correspondiente y definir el método __repr__
#para generar una cadena de una sola línea como sigue.
#directorio:valor_directorio:archivo:valor_archivo:extension:valor_extension
 
#Con la ruta de entrada crea un objeto con la clase implementada como se describió 
#y luego imprimélo 

#Nota: debes usar objetos y clases, se revisarán los códigos
class Ruta():
    def __init__(self, ruta):
        partes = ruta.split('/')
        if not '/' in ruta:
            self.directorio = './'
        else:
            self.directorio = '/'.join(partes[:-1]) + '/'

        self.archivo = partes[-1]
        self.extension = self.archivo.split('.')[-1]

    def __repr__(self):
        plantilla = 'directorio:%s:archivo:%s:extension:%s'
        return plantilla % (self.directorio,
                            self.archivo,
                            self.extension)


if __name__ == '__main__':
    ruta = input()
    objeto = Ruta(ruta)
    print(objeto)