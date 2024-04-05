def ordenar_por_longitud(tupla):
    return tuple(sorted(tupla, key=len))

if __name__ == "__main__":
    tupla = ("manzana", "pera", "banana", "uva", "naranja")
    resultado = ordenar_por_longitud(tupla)
    print("Tupla ordenada por longitud:", resultado)
