"""
⠀⠀⠀⠀⢀⠠⠤⠀⢀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠐⠀⠐⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⠀⢀⣼⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⣴⣿⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣇⠀⠀⢀⣾⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡟⠀⠀
⠀⠀⠀⠀⢰⡿⠉⠀⡜⣿⣿⣿⣿⣿⣿⣿⣿⠃.
⠀⠀⠒⠒⠸⣿⣄⢀⣃⣿⣿⡟⠉⠉⠉⢹⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠚⠉⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠘⠠⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠛⠛⠁⠀⠒⠤⠀⠀⠀⠀
⠨⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
╔═╗┌─┐┌┬┐┬ ┬┌─┐┬  ╔╦╗┌─┐┌┬┐┌┬┐┬ ┬
╠═╣│   │ │ │├─┤│  ║║║├─┤ ││ ││└┬┘
╩ ╩└─┘ ┴ └─┘┴ ┴┴─┘╩ ╩┴ ┴─┴┘─┴┘ ┴ 
github.com/madness14
"""

"""

Tuto rapido owo:
> En `inputs`, agrega las entradas que necesita el programa
  - Las entradas deben comenzar desde la línea 'inputs'
  - Separa cada entrada por líneas, como se muestra en el ejemplo.
> Asegúrate de que la ruta del archivo en `script_path` es correcta n.n
  - En Windows, verifica la ruta haciendo clic derecho en el archivo, 
  seleccionando "Propiedades" y copiando la "Ubicacion".
  - En Linux, puedes obtener la ruta completa del archivo usando el 
  comando `pwd` en el terminal y combinándolo con el nombre del archivo.
> El codigo configurará y ejecutará el script con las entradas proporcionadas.
> Si hay errores, se mostrarán, si no, debera verse la salida del programa ^-^

Ejemplo de uso:
Supongamos que tenemos un programa llamado `Ordenar.py` en Ubuntu que 
toma como entrada 'n' números enteros e imprime la lista ordenada.
Por ejemplo, si queremos ordenar los números 3, 2, 5, 4 y 1, debemos 
escribirlo así:

inputs = '''5 
3
2
5
4
1
'''

script_path = 'ruta/del/archivo/Ordenar.py'
Salida: [1, 2, 3, 4, 5]
"""


import subprocess
inputs = """
""" 

def ejecutar_programa():
    script_path = ''

    proceso = subprocess.Popen(
        ['python', script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = proceso.communicate(inputs)

    if proceso.returncode != 0:
        print(f"Error ejecutando el programa: {stderr}")
    else:
        print(f"Salida del programa:\n{stdout}")

if __name__ == '__main__':
    ejecutar_programa()