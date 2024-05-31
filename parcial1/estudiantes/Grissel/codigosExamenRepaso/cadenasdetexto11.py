# - - - Calcular si un año es bisiesto
anio = int(input("Ingrese un año: ")) # 2024
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.") # El año es bisiesto    
# - - - Convertir segundos a minutos y segundos:
segundos_totales = int(input("Ingrese la cantidad de segundos: ")) # 180
minutos = segundos_totales // 60
segundos_restantes = segundos_totales % 60
print(f"{segundos_totales} segundos son {minutos} minutos y {segundos_restantes} segundos.") # 180 segundos son 3 minutos y 0 segundos.

# Sustituciones
# - - - Sustitución de valores en una cadena de texto
nombre = input() # Grissel
edad = int(input()) # 19
mensaje = "Hola, %s. Tienes %d años." % (nombre, edad)
print(mensaje) # Hola, Grissel. Tienes 19 años.

# - - - Sustitución de valores en una cadena de formato
temperatura = 25.5
humedad = 60
informacion = "La temperatura es %.1f°C y la humedad es %d%%." % (temperatura, humedad)
print(informacion) # La temperatura es 25.5°C y la humedad es 60%.