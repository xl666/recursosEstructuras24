#Hacer un script que recibe un archivo de texto todo en minúsculas y genera un nuevo archivo de texto con todas las cadenas en mayúsculas
inicial = open(r'C:\Users\eduar\OneDrive\Escritorio\inicial.txt', 'tr') 
minusculas  = inicial.read()
mayusculas = minusculas.upper()
final = open(r'C:\Users\eduar\OneDrive\Escritorio\final.txt', 'tw') 
final.write(mayusculas)
inicial.close()
final.close()