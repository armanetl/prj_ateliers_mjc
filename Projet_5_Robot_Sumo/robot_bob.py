from robot import Robot
from moteur_bob import Moteur
from ultrason_bob import Ultrason
from PicoAutonomousRobotics import KitronikPicoRobotBuggy



class RobotBob(Robot):
    
    def __init__(self):
        self.kprb = KitronikPicoRobotBuggy()
        self.moteur_gauche = Moteur(self.kprb, 'l')
        self.moteur_droit = Moteur(self.kprb, 'r')
        self.us_avant = Ultrason(self.kprb)
    
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
