from machine import Pin, PWM
from servo import Servo
import time

moteur_bas=Servo(pin=3)
moteur_milieu=Servo(pin=4) 
moteur_haut=Servo(pin=5)


moteur_bas_min = 10
moteur_bas_max = 100
moteur_milieu_min = 90
moteur_milieu_max = 180
moteur_haut_min = 40
moteur_haut_max = 150

temps_attente = 0.1

def bras_repos():
    moteur_bas.move(moteur_bas_min) 
    moteur_milieu.move(moteur_milieu_min) 
    moteur_haut.move(moteur_haut_min) 
    time.sleep(temps_attente)

def servo_monte(moteur,angle_min,angle_max,vitesse):
    for angle in range (angle_min,angle_max):
        if (angle % vitesse == 0): 
            moteur.move(angle)
            time.sleep(temps_attente)
            
def servo_descend(moteur,angle_min,angle_max,vitesse):
    for angle in range (angle_max,angle_min,-1):
        if (angle % vitesse == 0):
            moteur.move(angle)
            time.sleep(temps_attente)

def bras_monte(vitesse):
    servo_monte(moteur_bas,moteur_bas_min,moteur_bas_max,vitesse)
    servo_monte(moteur_milieu,moteur_milieu_min,moteur_milieu_max,vitesse)
    servo_monte(moteur_haut,moteur_haut_min,moteur_haut_max,vitesse)

def bras_descend(vitesse):
    servo_descend(moteur_bas,moteur_bas_min,moteur_bas_max,vitesse)
    servo_descend(moteur_milieu,moteur_milieu_min,moteur_milieu_max,vitesse)
    servo_descend(moteur_haut,moteur_haut_min,moteur_haut_max,vitesse)


bras_repos()
bras_monte(10)
bras_descend(10)


