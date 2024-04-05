# - - - Sumar dos números
def suma(a, b):
    resultado = a + b
    return resultado

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    # Llamando a la función y almacenando resultado en variable
    resultado_suma = suma(a, b)
    print(resultado_suma)
    
# - - - Saludo personalizado
def saludar(nombre):
    mensaje = 'Hola, ' + nombre + ', ¿Cómo estás?'
    return mensaje

if __name__ == '__main__':
    nombre_usuario = input() #solicitar nombre
    #llamando a la función y mostrando mensaje
    print(saludar(nombre_usuario))
    