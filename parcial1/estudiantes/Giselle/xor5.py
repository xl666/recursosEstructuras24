# El operador lógico xor (or exclusivo) es similar a or, con la diferencia de que si ambos 
#operandos son verdaderos entonces el resultado es falso.

#Esta es la tabla de verdad correspondiente:

#0 0 0
#0 1 1
#1 0 1
#1 1 0

#Crea una función que recibe dos parámetros booleanos y realiza la operación xor.
#Tu solución sólo puede usar operadores or y and normales
a = input()
b = input ()
a = int (a)
b = int (b)

y = b ^ a
result = bool (y)

print(str(result))