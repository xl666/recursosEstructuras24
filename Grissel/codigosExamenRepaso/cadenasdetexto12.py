# - - - Formateo básico de cadenas
nombre = input()
edad = int(input())
mensaje = "Hola, {}. Tienes {} años.".format(nombre, edad)
print(mensaje) # Hola, Grissel. Tienes 19 años.

# - - - Especificación de índices de lugar y formatos
precio = float(input())
descuento = float(input())
precio_final = precio * (1 - descuento)
informacion = "El precio original es ${0:.2f}, con un descuento del {1:.0%}, el precio final es ${2:.2f}.".format(precio, descuento, precio_final)
print(informacion) # El precio original es $450.65, con un descuento del 20%, el precio final es $360.52.

# - - - Formateo de alineación y relleno
nombre = "Juan"
apellido = "Pérez"
telefono = "123456789"
informacion = "Nombre: {:<10} Apellido: {:>10} Teléfono: {:^10}".format(nombre, apellido, telefono)
print(informacion) # Nombre: Juan       Apellido:      Pérez Teléfono: 123456789 