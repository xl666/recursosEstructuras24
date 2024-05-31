# - - - Interpolación de variables en una cadena
nombre = "María"
edad = 25
mensaje = f"Hola, {nombre}. Tienes {edad} años."
print(mensaje)

# - - - Cálculo dentro de una cadena f
radio = float(input())
area = f"El área de un círculo con radio {radio} es {3.14 * radio ** 2}."
print(area) # El área de un círculo con radio 30.0 es 2826.0.

# - - - Usando expresiones más complejas en una cadena f
precio_unitario = float(input()) # 567.45
cantidad = int(input()) # 3
total = f"El total a pagar es: {precio_unitario * cantidad * (1 - 0.1)}."
print(total) # El total a pagar es: 1532.1150000000002.