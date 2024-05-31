def llenar_datos(n_usuario: int,nombre:str, dato:str)->str:
    """
    Llena un diccionarios con usuarios y sus datos personales, y regresa el dato del usuario
    que se pide.
    n_usuario:int, el número de usuarios que se introduciran
    nombre:str, el nombre del usuario del que se quiere obtener algún dato
    dato:str, el dato en específico que se quiere recuperar
    return:str, el dato que se solicitó  
    """
    datos_usuarios={}
    for i in range(n_usuario):
        usuario=input()
        nombre_usuario=usuario.split(':')[0]
        datos_usuarios[nombre_usuario]={}
        otro_datos=usuario.split('$')[1:]
        datos_usuarios[nombre_usuario]['algoritmo'],datos_usuarios[nombre_usuario]['salt'], datos_usuarios[nombre_usuario]['password']=otro_datos[0],otro_datos[1],otro_datos[2]
    return datos_usuarios[nombre][dato]


if __name__=='__main__':
    n_usuario=int(input())
    nombre=input()
    dato=input()
    print(llenar_datos(n_usuario, nombre, dato))