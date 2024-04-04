    #STRIP()
    # Elimina las caracteres especificos al inicio y al final de la cadena
    # Eliminara de defecto los espacios si no se indica ningun caracter.
    cadena = "  Hola Ciberseguridad  "
    resultado = cadena.strip()
    print(resultado)  # 'Hola Ciberseguridad'

    #UPPER()
    # Convierte todos los caracteres de la cadena a mayúsculas
    cadena = "hola ciberseguridad"
    resultado = cadena.upper()
    print(resultado)  # 'HOLA CIBERSEGURIDAD'

    #SPLIT()
    # Divide la cadena en una lista, utilizando el delimitador especificado
    cadena = "Uno, dos, tres"
    resultado = cadena.split(", ")
    print(resultado)  # ['Uno', 'dos', 'tres']

    #STARTSWITH()
    # Verifica si la cadena comienza con el prefijo especificado
    # Si se encuentra el prefijo retorna True , si no False
    cadea = "Estructura de datos"
    resultado = cadena.startswith("Estructura")
    print(resultado)  # True

    #ENDSWITH()
    # Verifica si la cadena termina con el sufijo especificado
    # Si termina con el prefijo retorna True, si no False
    cadena = "Hola civerseguridad"
    resultado = cadena.endswith("ciberseguridad")
    print(resultado)  # True

    # ISNUMERIC()
    #Verifica si todos los caracteres en la cadena son numéricos. 
    #Retorna True si todos los caracteres son numéricos, de lo contrario False.
    # Verifica si todos los caracteres en la cadena son numéricos
    cadena = "12345 , 25369 , 5424 , 4254"
    resultado = cadena.isnumeric()
    print(resultado)  # True

    #FORMAT()
    # Formatea la cadena de acuerdo con los argumentos proporcionados
    cadena = "Populacion mundial es: {}"
    populacion = "8 billones"
    resultado = s.format(populacion)
    print(resultado)  # 'Populacion mundial es: 8 billones'



