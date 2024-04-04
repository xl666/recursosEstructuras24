def eliminar (lista1):
 lista2 = [num for num in lista1 if not num (N)] 
 return lista2 
if __name__ == "__main__":
    N = int(input())
    M = int(input())
    lista1 = [int(input()) for _ in range (M)]
    print(eliminar (lista1))
