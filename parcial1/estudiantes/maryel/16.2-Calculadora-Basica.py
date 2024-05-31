n1 = input("Ingresa el primer numero ")
n2 = input("Ingresa un segundo numero ")
n1, n2 = (int(n1), int(n2))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""\nPara los numeros {n1} y {n2}
La suma es: {suma}
La resta es: {resta}
La multiplicacion es:  {multi}
La division es: {div}\n"""

print(mensaje)
