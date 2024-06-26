def suma_impares_recursiva(n):
    if n <= 0:
        return 0
    elif n % 2 == 1:  # Si n es impar
        return n + suma_impares_recursiva(n - 2)
    else:  # Si n es par, buscar el siguiente impar
        return suma_impares_recursiva(n - 1)

if __name__ == '__main__':
    n = int(input().strip())
    resultado = suma_impares_recursiva(n)
    print(resultado)