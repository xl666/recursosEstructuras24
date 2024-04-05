class RutaUnix:
    def __init__(self, ruta):
        self.ruta_completa = ruta
        # Divide la ruta en directorio y archivo
        partes = ruta.rsplit('/', 1)
        if len(partes) == 1:  # Si no hay directorio especificado
            self.directorio = './'
            self.archivo = partes[0]
        else:
            self.directorio = partes[0] + '/'
            self.archivo = partes[1]
        # Divide el archivo en nombre y extensión
        nombre, extension = self.archivo.rsplit('.', 1)
        self.extension = extension

    def __repr__(self):
        return f"directorio:{self.directorio}:archivo:{self.archivo}:extension:{self.extension}"


# Entrada
ruta_input = input().strip()

# Crear objeto RutaUnix
ruta_objeto = RutaUnix(ruta_input)

# Imprimir representación
print(ruta_objeto)
