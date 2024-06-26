def frutas_rojas_rec(n, frutas, indice = 0, resultado = None):
    if resultado is None: # ---> Inicializarresultado  
        resultado = []
    # ---> lista de frutas rojas    
    frutas_rojas = ['cereza', 'ciruela', 'manzana']
    # ---> Caso base: si indice ha alzanzado n, retorna el resultado
    if indice == n:
        return resultado
        
    fruta_actual = frutas[indice] # ---> fruta actual
    # ---> si la fruta actual esta en frutas rojas y no esta en el resultado, añadirla
    if fruta_actual in frutas_rojas and fruta_actual not in resultado:
        resultado.append(fruta_actual)
        
    return frutas_rojas_rec(n, frutas, indice + 1, resultado) # ---> con el siguiente indice
    

if __name__ == '__main__':
    n = int(input())
    frutas = [input() for _ in range(n)]
    resultado = frutas_rojas_rec(n, frutas)
    print(resultado)