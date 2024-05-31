class RutaUnix:
    def __init__(self, ruta):
        # Dividir la ruta en directorio y archivo
        if '/' in ruta:
            self.directorio, self.archivo = ruta.rsplit('/', 1)
            self.directorio += '/'  # Añadir la diagonal al final del directorio
        else:
            self.directorio = './'  # Directorio actual si no se especifica ruta
            self.archivo = ruta
        self.extension = self.archivo.split('.')[-1]  # Obtener la extensión
    
    def __repr__(self):
        # Formato especificado para la representación del objeto
        return f"directorio:{self.directorio}:archivo:{self.archivo}:extension:{self.extension}"

# Ejemplo 1
ruta1 = RutaUnix("/tmp/nuevo_directorio/archivo.txt")
print(ruta1)

# Ejemplo 2
ruta2 = RutaUnix("pinguino.com.png")
print(ruta2)
