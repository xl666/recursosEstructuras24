# palindromo
def palindromo(cadena):
    resultado = ''
    for i in range (len(cadena) + 1):
        if i > 0:
            resultado += cadena[-i]
    return resultado
        
if __name__ == '__main__':
    cadena = input()
    print(palindromo(cadena) == cadena)