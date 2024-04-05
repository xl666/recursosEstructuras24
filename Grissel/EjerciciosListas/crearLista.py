# - - - Crear una Lista
def crear_lista():
    lista = []
    for _ in range(n):
        numero = int(input())
        lista.append(numero)
    return lista
        
if __name__ == '__main__':
    n = int(input()) 
    print(crear_lista())