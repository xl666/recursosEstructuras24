class personaje:
#   Al usar el constructor estamos declarando que atributos del objeto se van a
#   inicializar
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida): #Se inicializan los self
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    
    def atributos(self):
        print(self.__nombre, ':', sep = '')
        print('-Fuerza:', self.__fuerza)
        print('-inteligencia:', self.__inteligencia)
        print('-defensa:', self.__defensa)
        print('-vida:', self.__vida)
    
    def Subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
    
    def Esta_vivo(self):
        return self.__vida > 0
    
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, 'Ha muerto')

    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, 'ha producido', daño, 'puntos de daño a', enemigo.__nombre)
        if enemigo.Esta_vivo():
            print(enemigo.__nombre, 'tiene:', enemigo.__vida, 'Puntos de vida')
        else:
            enemigo.__morir()

    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self,fuerza):
        if fuerza < 0:
            print('ERROR')
        else:
            self.__fuerza = fuerza

if __name__ == '__main__':
    mi_personaje = personaje('carlos', 10, 1, 5, 100)
    enemigo = personaje('Malo', 10, 1, 5, 100)   
    