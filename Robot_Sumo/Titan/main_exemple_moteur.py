from machine import Pin
from moteur import Moteur
import time 

def main_exemple_moteur_carre():
    print('PROG: main_exemple_moteur_carre')    
    
    #Definition Moteur1    
    io_1 =Pin(8 , Pin.OUT)
    io_2 =Pin(9 , Pin.OUT)
    mD = Moteur(io_1, io_2)
    
    #Definition Moteur2
    io_3 =Pin(10 , Pin.OUT)
    io_4 =Pin(11 , Pin.OUT)
    mG = Moteur(io_3, io_4)

    i = 0
    #while True:
    while (i < 5):
        print('Boucle numero:',i)
        
        #Moteur avance
        print('avance')
        mD.marcheAvant()
        mG.marcheAvant()
        time.sleep(1)

        #Moteur stop
        print('stop')
        mD.stop()
        mG.stop()
        time.sleep(0.2)

        #moteur tourne
        print('tourne droite')
        mG.marcheAvant()
        mD.marcheArriere()
        time.sleep(0.6)

        #Moteur stop
        print('stop')
        mD.stop()
        mG.stop()
        time.sleep(0.2)
        
        #Incremente la boucle
        i = i + 1


