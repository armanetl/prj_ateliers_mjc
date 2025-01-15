from robot import Robot
from moteur_picogo import Moteur
from ultrason_basic import Ultrason
from Motor_mjc import PicoGo
import time


class RobotPicoGo(Robot):
    
    def __init__(self):
        self.pico_go = PicoGo()
        self.moteur_gauche = Moteur(self.pico_go, 'l')
        self.moteur_droit = Moteur(self.pico_go, 'r')
        self.us_avant = Ultrason(trigger_pin=14, echo_pin=15)
    
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
    r2d2 = RobotPicoGo()
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
   