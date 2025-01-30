from machine import Pin,I2C
from robot import Robot
from moteur_titan import Moteur
from ultrason_basic import Ultrason
from neopixel import Neopixel
from buzzer import Buzzer
from machine_i2c_lcd import I2cLcd

import time


class RobotTitan(Robot):
    
    def __init__(self):
        #Moteur
        self.io_1 =Pin(8 , Pin.OUT)
        self.io_2 =Pin(9 , Pin.OUT)
        self.moteur_droit = Moteur(self.io_1, self.io_2)              
        self.io_3 =Pin(10 , Pin.OUT)
        self.io_4 =Pin(11 , Pin.OUT)
        self.moteur_gauche = Moteur(self.io_3, self.io_4)  
        self.vitesse_moyenne = 1 #Pas de vitesse sur la carte Cytron
        #Ultrason
        self.us_avant = Ultrason(trigger_pin=2, echo_pin=3)
        #Buzzer
        self.pin_buzzer = 22
        self.volume_moyen = 600
        self.buzzer = Buzzer(self.pin_buzzer)
        self.buzzer.set_volume(self.volume_moyen)
        self.buzzer.stop()
        #Neopixel
        self.pin_neopixel = 0 #Gauche
        self.pin_neopixel = 1 #Droit
        self.nombre_leds = 8
        self.leds = Neopixel(self.nombre_leds, 0, self.pin_neopixel, "GRB")
        #Telecommande IR
        self.pin_telecommande = 5
        self.Code_Touche_Haut   = 0x18
        self.Code_Touche_Droite = 0x5A
        self.Code_Touche_Bas    = 0x52
        self.Code_Touche_Gauche = 0x08
        #LCD
        self.oled_width = 16
        self.oled_height = 2
        self.oled_color = 0 #Oled basic, no color
        self.pin_i2c_sda = 16
        self.pin_i2c_scl = 17
        self.i2c_num = 0
        self.i2c_dev = I2C(self.i2c_num, scl=Pin(self.pin_i2c_scl), sda=Pin(self.pin_i2c_sda), freq=200000)
        self.addr = self.i2c_dev.scan()[0]
        self.oled = I2cLcd(self.i2c_dev, self.addr, self.oled_height, self.oled_width)
        #Detecteurs de ligne
        #***FAIRE DES FCTS POUR EXTRAIRE L INFO***TROP DIFFERENTS SELON LES ROBOTS

        
    # controle d'un moteur ou de plusieurs moteur
    # moteur : "droit, "gauche"
    # ordre : "avant", "arriere", "stop"
    # vitesse : vitesse du moteur
    def moteur(self, moteur:str(), ordre:str(), vitesse=50):
        _mot = self.moteur_gauche
        if "droit" == moteur:
            _mot = self.moteur_droit
            
        if "avant" == ordre :
            _mot.marcheAvant()
        elif "arriere" == ordre :
            _mot.marcheArriere()
        else :
            _mot.stop()
                
    # obtient la distance d'un ou plusieurs détecteur
    # detecteur : "avant"
    def distance_cm(self, detecteur):
        return self.us_avant.distance_cm()

if __name__ == '__main__':
    print('test classe robot')    
    # declare le robot
    r2d2 = RobotTitan()
    # lecture de la distance
    distance = r2d2.distance_cm("avant")
    print('Distance:', "{0:2.2f}".format(distance), 'cm')
    # avance
    print('Avance')
    r2d2.moteur("droit","avant",60)
    r2d2.moteur("gauche","avant",60)
    time.sleep(0.6)    
    # stop
    r2d2.moteur("droit","stop",60)
    r2d2.moteur("gauche","stop",60)
    time.sleep(0.6)    
    # recule
    print('Recule')
    r2d2.moteur("droit","arriere",60)
    r2d2.moteur("gauche","arriere",60)
    time.sleep(0.6)    
    # stop
    r2d2.moteur("droit","stop",60)
    r2d2.moteur("gauche","stop",60)
    time.sleep(0.6)    
    # tourne
    print('Tourne')
    r2d2.moteur("droit","avant",60)
    r2d2.moteur("gauche","arriere",60)
    time.sleep(0.6)    
    # stop
    r2d2.moteur("droit","stop",60)
    r2d2.moteur("gauche","stop",60)
    time.sleep(0.6)    
    # tourne
    print('Tourne de l autre cote')
    r2d2.moteur("droit","arriere",60)
    r2d2.moteur("gauche","avant",60)
    time.sleep(0.6)    
    # stop
    r2d2.moteur("droit","stop",60)
    r2d2.moteur("gauche","stop",60)
    time.sleep(0.6)    
   