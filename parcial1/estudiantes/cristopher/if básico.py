
def Mes(Entrada):
    Meses = {1: 'Enero', 2:'Febrero', 3: 'marzo', 4: 'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre' }
    return Meses[Entrada]

        
if __name__ == '__main__':
    Entrada = int(input())

    if Entrada <= 0:
        print('No se puede')
    elif Entrada > 12:
        print('No se puede')
    else:
        print(Mes(Entrada))