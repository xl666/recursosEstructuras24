#Forma: identificador = expresion 

# Ejemplos
x = 5
x = 5 + 5
x = 5 + 5 * 5 # 30, primero se evalúa 5 * 5
x = (5 + 5) * 5 # 50, primero se evalúa 5 + 5
x = suma(5, 5) # invocación a función
x = suma(5, 5) - 1 # válido porque ambas son expresiones enteras
x = 'hola' # cadena, se puede cambiar el tipo
x = 'hola ' + 'mundo' # válido porque + se refiere a concatenación
x = 'hola' + 4 # error, incompatibilidad de tipos
y = 4
x += y # equivalente a x = x + y, hay variantes -=, *=, /=, %=
x = 4**2 # 4 elevado al cuadrado
x = 4 % 2 # operación de módulo
t = True or False
t = not t # intercambiar valor de verdad
b = 4 < 5 # b es True
b = 4 != 4 # b es False