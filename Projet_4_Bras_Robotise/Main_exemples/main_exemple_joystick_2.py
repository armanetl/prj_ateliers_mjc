#=====================================================
# Main Exemple Joystick:
# - Récupérer les valeurs x et y
# - En fonction des fonctions, définir une position AVANT,ARRIERE, DROITE,GAUCHE
#=====================================================
from machine import Pin, ADC
import utime

Axe_x = ADC(Pin(26))
Axe_y = ADC(Pin(27))

position = "CENTRE"

while True:
    Valeur_x = Axe_x.read_u16()
    Valeur_y = Axe_y.read_u16()
    #print("X: " + str(Valeur_x) + ", Y: " + str(Valeur_y))
    
    if ((Valeur_x < 3000) and ((Valeur_y > 50000) and (Valeur_y < 52000))):
        position = "GAUCHE"

    elif ((Valeur_x == 65535) and (Valeur_y == 65535)):
        position = "DROITE"
        
    elif ((Valeur_x > 60000) and (Valeur_x != 65535) and (Valeur_y == 65535)):
        position = "AVANT"
        
    elif (((Valeur_x > 49000) and (Valeur_x < 51000)) and (Valeur_y < 2000)):
        position = "ARRIERE"
    else:
        position = "CENTRE"
         
    print(position)
    utime.sleep(0.2)
