def crear_subdic(infos):
    valor = []
    llaves = ['algoritmo', 'salt', 'password']
    lista = []

    for i in range(len(infos)):
        for j in range(len(infos[i])):
            if j % 2 != 0:
                valor.append(infos[i][j].split('$'))

    for i in range(len(valor)):
        subdic = {}
        for j in range(1, len(valor[i])):
            subdic[llaves[j - 1]] = valor[i][j]
        lista.append(subdic)

    return lista

def crearDic(infos):
    subdic = crear_subdic(infos)
    dic = {}
    llaves = []
    for i in range(len(infos)):
        for j in range(len(infos[i])):
            if j % 2 == 0:
                llaves.append(infos[i][j])
    for i in range(len(llaves)):
        for j in range(len(llaves[i])):
            dic[llaves[i]] = subdic[i]
    
    return dic

def encontrarCampo(usuario, campo, infos):
    dic = crearDic(infos)
    for llave, valor in dic.items():
        if usuario == llave:
            usu = dic[usuario]
            for subllave, subvalor in usu.items():
                if subllave == campo:
                    return usu[subllave]

if __name__ == '__main__':
    n = int(input())
    usuario = input()
    campo = input()
    info = []
    infos = []
    for _ in range(n):
        info.append(input())

    for cadena in info:
        infos.append(cadena.split(':'))    

    print(encontrarCampo(usuario, campo, infos))