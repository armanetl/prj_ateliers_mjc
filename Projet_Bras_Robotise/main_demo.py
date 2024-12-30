from machine import Pin, PWM, ADC
from servo import Servo
from main_exemple_bras_1_classe import Bras
from main_exemple_joystick_2_classe import Joystick
import time

Axe_x = ADC(Pin(26))
Axe_y = ADC(Pin(27))
Joystick = Joystick(Axe_x,Axe_y)

moteur_bas=Servo(pin=3)
moteur_milieu=Servo(pin=4) 
moteur_haut=Servo(pin=5)

Bras = Bras(moteur_bas,moteur_milieu,moteur_haut)

Bras.bras_repos()

while True:
    position = Joystick.donne_position()
    print(position)
    if (position == "HAUT"):
        Bras.bras_monte(20)
    if (position == "BAS"):
        Bras.bras_descend(20)
    time.sleep(0.5)
        
