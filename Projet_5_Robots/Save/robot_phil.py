from machine import Pin
from robot import Robot
from moteur import Moteur
from ultrason import Ultrason




class RobotPhil(Robot):
    
    def __init__(self):
        #Definition Moteur1    
        self.io_1 =Pin(13 , Pin.OUT)
        self.io_2 =Pin(12 , Pin.OUT)
        self.io_pwm =Pin(11 )
        self.moteur_droit = Moteur(self.io_1, self.io_2, self.io_pwm)              
        #Definition Moteur2
        self.io_3 =Pin(17 , Pin.OUT)
        self.io_4 =Pin(16 , Pin.OUT)
        self.io_pwm2 =Pin(18 )
        self.moteur_gauche = Moteur(self.io_3, self.io_4, self.io_pwm2)   
        #Definition Ultrason
        self.us_avant = Ultrason(trigger_pin=1, echo_pin=0)
    
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
