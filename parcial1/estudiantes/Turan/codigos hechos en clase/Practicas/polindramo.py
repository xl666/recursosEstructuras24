def polindramo(texto):
    reversed_text = list(reversed(texto))
    texto = list(texto)
    if reversed_text == texto:
        return True
    else:
        return False
    


if __name__ == '__main__':
    texto =input('')
    resultado = polindramo(texto)
    print(resultado)
