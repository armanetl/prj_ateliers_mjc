#=====================================================
# Main Exemple Joystick:
# - Récupérer les valeurs x et y et les afficher sur l'ecran
#=====================================================
from machine import Pin, ADC
import utime

Axe_x = ADC(Pin(26))
Axe_y = ADC(Pin(27))

while True:
    Valeur_x = Axe_x.read_u16()
    Valeur_y = Axe_y.read_u16()
    print("X: " + str(Valeur_x) + ", Y: " + str(Valeur_y))
    utime.sleep(0.2)