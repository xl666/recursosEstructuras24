lista = [10, 20, 30, 40, 50]
valor = 40

def pertenece():
    for i in lista:
        if i == valor:
            return True
    return False
    
print(pertenece())
