import sys

def extract_hidden_file(ruta_pdf, ruta_salida):
    tamaño = 100
    PADDING = b'0' * tamaño

    with open(ruta_pdf, 'rb') as salida:
        while True:
            chunk = salida.read(tamaño)
            if len(chunk) < tamaño:
                break

            if chunk == PADDING:
                datos = salida.read()
                with open(ruta_salida, 'wb') as salida:
                    salida.write(datos)
                break


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <ruta_del_archivo_entrada> <ruta_del_archivo_salida>")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        extract_hidden_file(input_path, output_path)
