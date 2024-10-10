from machine import Pin

from moteur import Moteur
import time

#Initialisation de la classe

def main_Youssef_carre():
    # definition moteur 1
    io1 = Pin(8,Pin.OUT)
    io2 = Pin(9,Pin.OUT)
    m1 = Moteur(io1,io2)
    # definition moteur 2
    io3 = Pin(10,Pin.OUT)
    io4 = Pin(11,Pin.OUT)
    m2 = Moteur(io3,io4)

    while True:
        
        # moteur avance
        print('avance')
        m1.marcheAvant()
        m2.marcheAvant()
        time.sleep(1)
        # moteur stop
        print('arrete toi')
        m1.stop()
        m2.stop()
        #moteur tourne a gauche
        print('toune a gauche')
        m1.marcheArriere()
        m2.marcheAvant()
        time.sleep(0.6)
        #moteur stop
        m1.stop()
        m2.stop()