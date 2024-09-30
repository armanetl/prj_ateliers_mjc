from machine import Pin, PWM
from PicoAutonomousRobotics import KitronikPicoRobotBuggy
import utime
import time

class Moteur:
    def __init__(self, kprBuggy, moteur_cote = 'l'):
        self.kpr = kprBuggy
        self.moteur_cote =  moteur_cote
        self.stop()
        print('pense a mettre le switch a ON')
        
    def marche_avant(self, vitesse=50):
        self.kpr.motorOn(self.moteur_cote, 'f',vitesse)
        
    def marche_arrière(self, vitesse=50):
        self.kpr.motorOn(self.moteur_cote, 'r',vitesse)

    def stop(self):
        self.kpr.motorOff(self.moteur_cote)
        
    def roue_libre(self):
        print('not implemented')

if __name__ == '__main__':
    print('Test pilote pour deux moteurs avec boutons')

    kprb = KitronikPicoRobotBuggy()
    # Initialisation des moteurs
    moteur1 = Moteur(kprb, 'l')
    moteur2 = Moteur(kprb, 'r')
    moteur1.marche_avant()
    moteur2.marche_avant()

