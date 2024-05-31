n1 = input("Ingresa el primer numero ")
n2 = input("Ingresa un segundo numero ")
operacion = input("Ingresa la operacion a realizar(+,-,*,/) ")
n1, n2 = (int(n1), int(n2))
if operacion == "+":
    print("La suma de ", n1, " y ", n2, " es: ", n1 + n2)
elif operacion == "-":
    print("La resta de ", n1, " y ", n2, " es: ", n1 - n2)
elif operacion == "*":
    print("La multiplicacion de ", n1, " y ", n2, " es: ", n1 * n2)
elif operacion == "/":
    print("La division de ", n1, " y ", n2, " es: ", n1 / n2)
else:
    print("Ingresa una operacion correcta")
