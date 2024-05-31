numerodelmes=int(input ("Dame un numero entre 1 y 12: "))
listanombremes=["enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]

if numerodelmes > 12 or numerodelmes<1:
    print("Opcion no valido")

else:
    print(listanombremes[numerodelmes-1])


#Version del maestro
    mes= int(intput())
   def regresar_mes(mes): #podrias ser X lugar mes.
        listademeses=[e,f,m,a,m,j,j,a,s,o,n,d] 
        return listademeses[mes-1]
    regresar_mes

#Version del maestro 2
def regresar mes2(mes ):
    diccionario_meses= {1: 'enero ', 2: 'febrero'}
    return diccionario_meses[mes]

regresar_mes(mes)