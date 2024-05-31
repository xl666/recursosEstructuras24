def sumatoria_columnas(F, C, matriz):
  columnas_sumas = [0] * C
  for i in range(F):
    for j in range(C):
      columnas_sumas[j] += matriz[i * C + j]
  return columnas_sumas

# Ejemplo de uso
F = int(input())
C = int(input())
matriz = [int(x) for x in input().split()]

# Calcular la sumatoria de las columnas
columnas_sumas = sumatoria_columnas(F, C, matriz)

# Imprimir la salida
print(",".join(map(str, columnas_sumas)))
