def cifrado_cesar(shift, texto):
    texto_cifrado = ""
    for caracter in texto:
        if caracter == " ":
            texto_cifrado += " "
            continue
        codigo = ord(caracter) - ord('a')
        nuevo_codigo = (codigo + shift) % 26
        nuevo_caracter = chr(ord('a') + nuevo_codigo)
        texto_cifrado += nuevo_caracter
    return texto_cifrado
5
shift = int(input())
texto = input()

texto_cifrado = cifrado_cesar(shift, texto)

print(texto_cifrado)