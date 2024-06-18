# Capitalizar nombre propio - - - - - - - - - - - - - - - - - - - - - - - - - - 
def capitalizar(cadena):
    excepciones = ['de', 'la']
    partes = cadena.split(' ')
    
    resultado = []
    for palabra in partes:
        if palabra in excepciones:
            resultado.append(palabra)
        else:
            resultado.append(palabra.capitalize())
            
    nombre_capitalizado = ' '.join(resultado) 
    return nombre_capitalizado       

if __name__ == '__main__':
    cadena = input()
    capitalizar_nombre = capitalizar(cadena)
    print(capitalizar_nombre)