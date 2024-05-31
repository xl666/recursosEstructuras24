texto = input()
archivo = open(r'C:\Users\eduar\OneDrive\Escritorio\mayusculas.txt', 'tw')
archivo.write(texto.upper())
archivo.close()
