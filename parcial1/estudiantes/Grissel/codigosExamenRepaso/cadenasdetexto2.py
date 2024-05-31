# - - - Ejemplo 1: Cadena de longitud 1
s2 = 'a'
print(s2[0])  # Imprime el único carácter de la cadena, que es 'a'.
print(s2[-1]) # Imprime el único carácter de la cadena, que es 'a'.
print(s2[len(s2)-1]) # Imprime también el único carácter de la cadena, que es 'a'.

# - - - Ejemplo 2: Cadena con varios caracteres
s3 = 'python'
print(s3[0])  # Imprime el primer carácter de la cadena, que es 'p'.
print(s3[-1]) # Imprime el último carácter de la cadena, que es 'n'.
print(s3[len(s3)-1]) # Imprime también el último carácter de la cadena, que es 'n'.

print("My father's house")
print('My father\'s house') # se escapa la '
print('Primera línea\nSegunda línea')
print('\tCon sangría')

s = '''Esta es una
cadena de varias líneas
útil para crear formatos de texto
o documentar funciones y módulos
'''
print(s)
        