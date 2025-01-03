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

def motor_stable():
    moteur_bas.move(moteur_bas_min) 
    moteur_milieu.move(moteur_milieu_min) 
    moteur_haut.move(moteur_haut_min) 
    time.sleep(temps_attente)

def test_amplitude(moteur,angle_min,angle_max):
    for angle in range (angle_min,angle_max):
        if (angle % 2 == 0): #De 2 en 2
            moteur.move(angle)
            time.sleep(temps_attente)
    for angle in range (angle_max,angle_min,-1):
        if (angle % 2 == 0):
            moteur.move(angle)
            time.sleep(temps_attente)


motor_stable() #Position Min
test_amplitude(moteur_bas,moteur_bas_min,moteur_bas_max)
test_amplitude(moteur_milieu,moteur_milieu_min,moteur_milieu_max)
test_amplitude(moteur_haut,moteur_haut_min,moteur_haut_max)

