nombre = input()
nombre2 = []
casosespeciales = ["de", "la"]

for i in nombre.split(' '):
    if i in casosespeciales:
        nombre2.append(i)
    else:
        nombre2.append(i.capitalize())

capitalizar = ' '.join(nombre2)

print(capitalizar)