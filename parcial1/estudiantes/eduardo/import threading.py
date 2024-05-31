import threading
import time

def hola(nombre):
    while True:
        print('hola' + nombre)
        time.sleep(1)

def adios(nombre):
    while True:
     print('adios' + nombre)
     time.sleep(1)

h1 = threading.Thread(target=hola, args=(' pepe',))
h2 = threading.Thread(target=adios, args=(' pepe',))
h1.start()
h2.start()