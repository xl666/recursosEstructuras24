def suma_columnas(matriz):
    filas = len(matriz)
    columnas = max(len(fila) for fila in matriz)  # Obtiene el máximo número de columnas
    
    # Creamos una lista para almacenar las sumas de cada columna
    suma_columnas = [0] * columnas
    
    # Iteramos sobre cada fila y columna para calcular la suma de cada columna
    for fila in matriz:
        for j in range(len(fila)):
            suma_columnas[j] += fila[j]
    
    return suma_columnas

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5],
    [7, 8, 9, 10]
]

sumas = suma_columnas(matriz)
print("Suma de cada columna:", sumas)