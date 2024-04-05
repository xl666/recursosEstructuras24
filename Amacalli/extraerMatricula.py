import re

def elementos (num_nombres):
    cadenas = []
    for _ in range(num_nombres):
        cadenas.append(input())
    return cadenas

def obtener_matriculas(cadenas):
    matriculas = []
    for cadena in cadenas:
        match = re.search(r'\((.*?)\)', cadena)
        if match:
            matricula = match.group(1) 
            matriculas.append(matricula)
    return matriculas

if __name__ == "__main__":
    num_nombres = int(input())
    cadenas = elementos(num_nombres)
    
    matriculas = obtener_matriculas(cadenas)
    print()
    for matricula in matriculas:
        print(matricula)
