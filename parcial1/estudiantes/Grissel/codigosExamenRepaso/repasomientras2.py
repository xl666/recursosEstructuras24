# - - - Búsqueda de un número 
def encontrar_numero(numero_a_buscar):
    numero = 1
    while True:
        if numero == numero_a_buscar:
            print(f"Número {numero_a_buscar} encontrado!")
            break
        print("Buscando...")
        numero += 1

if __name__ == '__main__':
    numero_buscado = int(input())
    encontrar_numero(numero_buscado)
    
# - - - Impresion de números pares
def imprimir_numeros_pares():
    inicio = int(input())
    fin = int(input())
    print("Números pares en el rango:")
    numero_actual = inicio
    while numero_actual <= fin:
        if numero_actual % 2 != 0:  # Si el número es impar, omitirlo
            numero_actual += 1
            continue
        print(numero_actual)
        numero_actual += 2  # Saltar al siguiente número par

if __name__ == '__main__':
    imprimir_numeros_pares()