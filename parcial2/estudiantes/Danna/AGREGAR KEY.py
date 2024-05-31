def llenardic() -> dict:
    diccionario = {
        'nombre': input(),
        'edad': input(),
        'ciudad': input()
    }
    return diccionario

def accederdic(dic: dict)->dict:
    for k, v in dic.items():
        print(k, ':', v)
        return dic
    

def cambiar_dic (dic: dict)->dict:
    dic['prefesion']=input()
    return dic

if __name__=='__main__':
    dic=llenardic()
    print (accederdic(dic))
    dic= cambiar_dic(dic)
    print (accederdic(dic))
    