def contador(x):
    counter = 0
    anterior = None
    for caracter in x:
        if caracter == "." and anterior != ".":
                counter += 1
        anterior = caracter
    print(counter)
    
cadena=str(input())
contador(cadena)