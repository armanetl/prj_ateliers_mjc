from machine import Pin
from robot import Robot
from moteur_titan import Moteur
from ultrason import Ultrason




class RobotTitan(Robot):
    
    def __init__(self):
        #Definition Moteur1    
        self.io_1 =Pin(8 , Pin.OUT)
        self.io_2 =Pin(9 , Pin.OUT)
        self.moteur_droit = Moteur(self.io_1, self.io_2)              
        #Definition Moteur2
        self.io_3 =Pin(10 , Pin.OUT)
        self.io_4 =Pin(11 , Pin.OUT)
        self.moteur_gauche = Moteur(self.io_3, self.io_4)   
        #Definition Ultrason
        self.us_avant = Ultrason(trigger_pin=2, echo_pin=3)
    
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
