def evalMatriz (matriz):
    if type(matriz) is list:
        col = len(matriz[0])
        for i in range(len(matriz)):
            if type(matriz[i]) is list:
                if col != len(matriz[i]):
                    return False
            else:
                return False
        
    else:
        return False
    
    return True

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(evalMatriz(matriz))