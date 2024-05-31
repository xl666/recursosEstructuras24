def cifrado_cesar(frase, salto):
    res = ""
    for caracter in frase:
        if caracter.isalpha():  
            
            codigo = ord(caracter) - ord('a')
            
            nuevocodigo = (codigo + salto) % 26
            
            letra = chr(ord('a') + nuevocodigo)
            res += letra
        else:
            
            res += caracter
    return res


salto = int(input())
cadena = str(input())


resultado_cifrado = cifrado_cesar(cadena, salto)
print(resultado_cifrado)