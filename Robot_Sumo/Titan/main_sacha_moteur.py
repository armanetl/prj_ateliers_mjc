from machine import Pin
import time 
from moteur import Moteur

def main_Sacha_carre():

    moteur_g = Moteur(Pin(8,Pin.OUT),
                    Pin(9,Pin.OUT))

    moteur_d = Moteur(Pin(10,Pin.OUT),
                    Pin(11,Pin.OUT))

    moteur_g.marcheAvant()
    moteur_d.marcheAvant()
    time.sleep(0.2)

    moteur_g.stop()
    moteur_d.stop()
    time.sleep(0.3)

    moteur_g.marcheAvant()
    moteur_d.marcheArriere()
    time.sleep(0.2)

    moteur_g.marcheAvant()
    moteur_d.marcheAvant()
    time.sleep(2)

    moteur_g.stop()
    moteur_d.stop()
    time.sleep(0.3)

    moteur_g.marcheAvant()
    moteur_d.marcheArriere()
    time.sleep(0.2)

    moteur_g.marcheAvant()
    moteur_d.marcheAvant()
    time.sleep(0.2)

    moteur_g.stop()
    moteur_d.stop()
    time.sleep(0.3)

    moteur_g.marcheAvant()
    moteur_d.marcheArriere()
    time.sleep(0.2)

    moteur_g.marcheAvant()
    moteur_d.marcheAvant()
    time.sleep(0.2)

    moteur_g.stop()
    moteur_d.stop()
    time.sleep(0.3)

    moteur_g.marcheAvant()
    moteur_d.marcheArriere()
    time.sleep(0.2)

    moteur_g.stop()
    moteur_d.stop()
