#Dado un número N de cadenas con información de alumnos
#que incluye nombre completo y matrícula en el siguiente formato:
#nombre completo (matrícula)
#Regresa sólo la matrícula (sin paréntesis)
def obtener_matriculas(cadenas_alumnos):
    matriculas = []
    for cadena in cadenas_alumnos:
        inicio_matricula = cadena.find('(') + 1
        fin_matricula = cadena.find(')')
        matricula = cadena[inicio_matricula:fin_matricula]
        matriculas.append(matricula)
    return matriculas

num_cadenas = int(input())
cadenas_alumnos = []
for _ in range(num_cadenas):
    cadena = input()
    cadenas_alumnos.append(cadena)

matriculas_alumnos = obtener_matriculas(cadenas_alumnos)
for matricula in matriculas_alumnos:
    print(matricula)

    
