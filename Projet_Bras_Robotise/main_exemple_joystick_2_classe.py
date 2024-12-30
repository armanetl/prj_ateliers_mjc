#=====================================================
# Classe Joystick
#=====================================================
from machine import Pin, ADC
import utime

class Joystick:
    def __init__(self, Axe_x, Axe_y):
        self.Axe_x = Axe_x
        self.Axe_y = Axe_y
        self.position = "CENTRE"
    
    def donne_position(self):
        self.Valeur_x = self.Axe_x.read_u16()
        self.Valeur_y = self.Axe_y.read_u16()
        #print("X: " + str(self.Valeur_x) + ", Y: " + str(self.Valeur_y))
        if ((self.Valeur_x < 3000) and ((self.Valeur_y > 50000) and (self.Valeur_y < 52000))):
            self.position = "DROITE"

        elif ((self.Valeur_x == 65535) and (self.Valeur_y == 65535)):
            self.position = "GAUCHE"
            
        elif ((self.Valeur_x > 60000) and (self.Valeur_x != 65535) and (self.Valeur_y == 65535)):
            self.position = "HAUT"
            
        elif (((self.Valeur_x > 49000) and (self.Valeur_x < 51000)) and (self.Valeur_y < 2000)):
            self.position = "BAS"
        else:
            self.position = "CENTRE"
        return self.position

if __name__ == '__main__':
    Axe_x = ADC(Pin(26))
    Axe_y = ADC(Pin(27))
    Joystick = Joystick(Axe_x,Axe_y)
    while True:
        position = Joystick.donne_position()
        print(position)
        utime.sleep(0.2)
