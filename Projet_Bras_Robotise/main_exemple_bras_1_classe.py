#=====================================================
# Classe Bras
#=====================================================
from machine import Pin, PWM
from servo import Servo
import time

class Bras:
    def __init__(self, moteur_bas, moteur_milieu,moteur_haut):
        self.moteur_bas = moteur_bas
        self.moteur_milieu = moteur_milieu
        self.moteur_haut = moteur_haut
        
        self.moteur_bas_min = 10
        self.moteur_bas_max = 100
        self.moteur_bas_current = self.moteur_bas_min
        
        self.moteur_milieu_min = 90
        self.moteur_milieu_max = 180
        self.moteur_milieu_current = self.moteur_milieu_min
        
        self.moteur_haut_min = 40
        self.moteur_haut_max = 150
        self.moteur_haut_current = self.moteur_haut_min
        
        self.temps_attente = 0.1

    def bras_repos(self):
        self.moteur_bas.move(self.moteur_bas_min) 
        self.moteur_milieu.move(self.moteur_milieu_min) 
        self.moteur_haut.move(self.moteur_haut_min) 
        time.sleep(self.temps_attente)

    def servo_monte(self,moteur,angle_min,angle_max,vitesse):
        for angle in range (angle_min,angle_max):
            if (angle % vitesse == 0): 
                moteur.move(angle)
                time.sleep(self.temps_attente)
                
    def servo_descend(self,moteur,angle_min,angle_max,vitesse):
        for angle in range (angle_max,angle_min,-1):
            if (angle % vitesse == 0):
                moteur.move(angle)
                time.sleep(self.temps_attente)

    def bras_monte(self,vitesse):
        if (self.moteur_bas_current != self.moteur_bas_max):
            self.servo_monte(self.moteur_bas,self.moteur_bas_min,self.moteur_bas_max,vitesse)
            self.moteur_bas_current = self.moteur_bas_max
        if (self.moteur_milieu_current != self.moteur_milieu_max):
            self.servo_monte(self.moteur_milieu,self.moteur_milieu_min,self.moteur_milieu_max,vitesse)
            self.moteur_milieu_current = self.moteur_milieu_max
        if (self.moteur_haut_current != self.moteur_haut_max):
            self.servo_monte(self.moteur_haut,self.moteur_haut_min,self.moteur_haut_max,vitesse)
            self.moteur_haut_current = self.moteur_haut_max

    def bras_descend(self,vitesse):
        if (self.moteur_bas_current != self.moteur_bas_min):
            self.servo_descend(self.moteur_bas,self.moteur_bas_min,self.moteur_bas_max,vitesse)
            self.moteur_bas_current = self.moteur_bas_min
        if (self.moteur_milieu_current != self.moteur_milieu_min):
            self.servo_descend(self.moteur_milieu,self.moteur_milieu_min,self.moteur_milieu_max,vitesse)
            self.moteur_milieu_current = self.moteur_milieu_min
        if (self.moteur_haut_current != self.moteur_haut_min):
            self.servo_descend(self.moteur_haut,self.moteur_haut_min,self.moteur_haut_max,vitesse)
            self.moteur_haut_current = self.moteur_haut_min

if __name__ == '__main__':  
    moteur_bas=Servo(pin=3)
    moteur_milieu=Servo(pin=4) 
    moteur_haut=Servo(pin=5)
    Bras = Bras(moteur_bas,moteur_milieu,moteur_haut)
    Bras.bras_repos()
    Bras.bras_monte(10)
    Bras.bras_descend(10)
    time.sleep(1)
