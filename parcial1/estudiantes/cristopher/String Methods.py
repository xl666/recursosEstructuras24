name = input()

#Obtains the lenght of a string 
print(len(name))

#Obtains the position of a character 
print(name.find('i'))

#Obtains the last apparence of a character
print(name.rfind('s'))

#Incluye una mayuscula al inicio 
print(name.capitalize())

#Pasa toda la cadena a mayusculas
print(name.upper())

#Pasa a minusculas la caena 
print(name.lower())

#Verifica si son numeros
print(name.isdigit())

#Verifica si son caracteres 
print(name.isalpha())

#Count de number of apparences of a character 
print(name.count('s'))

#Change a character in a string
nuevo_nombre = name.replace('c',"p")
print(nuevo_nombre)

#quita espacios al inicio o al final
print(name.strip())

#Cada palabra se convierte en un objeto de una lista
print(name.split('c'))

#Sirve para añadir placeholders
print('Hola mi nombre es {name}'.format(name = 'cris'))

#Devuelve true si termina con el caracter
print(name.endswith('s'))

#Devuelve true si empieza con el caracter
print(name.startswith('c'))

#Sirve para pasaar caracteres a lista
print(''.join(name))