from robot import Robot
from moteur_yaboom import Moteur
from ultrason_yaboom import Ultrason
from pico_car_mjc import pico_car
from pico_car_mjc import ultrasonic
from neopixel import Neopixel
from buzzer import Buzzer
from ssd1306 import SSD1306_I2C

from machine import Pin,I2C
import time


class RobotYaboom(Robot):
    
    def __init__(self):
        self.pico_car = pico_car()
        #Moteur
        self.moteur_gauche = Moteur(self.pico_car, 'l')
        self.moteur_droit = Moteur(self.pico_car, 'r')
        self.vitesse_moyenne = 70
        #Ultrason
        self.ultrasonic = ultrasonic()
        self.us_avant = Ultrason(self.ultrasonic)
        #Buzzer
        self.pin_buzzer = 22
        self.volume_moyen = 600
        self.buzzer = Buzzer(self.pin_buzzer)
        self.buzzer.set_volume(self.volume_moyen)
        self.buzzer.stop()
        #Neopixel
        self.pin_neopixel = 6
        self.nombre_leds = 8
        self.leds = Neopixel(self.nombre_leds, 0, self.pin_neopixel, "GRB")
        #Telecommande IR
        self.pin_telecommande = 7
        self.Code_Touche_Haut   = 0x01
        self.Code_Touche_Droite = 0x06
        self.Code_Touche_Bas    = 0x09
        self.Code_Touche_Gauche = 0x04
        #Oled 128x32
        self.oled_width = 128
        self.oled_height = 32
        self.oled_color = 0 #Oled basic, no color
        self.pin_i2c_sda = 14
        self.pin_i2c_scl = 15
        self.i2c_num = 1
        self.i2c_dev = I2C(self.i2c_num, scl=Pin(self.pin_i2c_scl), sda=Pin(self.pin_i2c_sda), freq=200000)
        self.oled = SSD1306_I2C(128, 32, self.i2c_dev)
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
            _mot.marcheAvant(vitesse)
        elif "arriere" == ordre :
            _mot.marcheArriere(vitesse)
        else :
            _mot.stop()
                
    # obtient la distance d'un ou plusieurs détecteur
    # detecteur : "avant"
    def distance_cm(self, detecteur):
        return self.us_avant.distance_cm()


if __name__ == '__main__':
    print('test classe robot')    
    # declare le robot
    r2d2 = RobotYaboom()
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
    
