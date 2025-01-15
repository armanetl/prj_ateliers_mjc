#from robot_yaboom import RobotYaboom
#from robot_picogo import RobotPicoGo
#from robot_titan import RobotTitan
from robot_goliath import RobotGoliath
#from robot_phil import RobotPhil
#from robot_bob import RobotBob
import time

def main_exemple_deplacement_robot():

    # declare le robot
    #r2d2 = RobotYaboom()
    #vitesse = 70
    #r2d2 = RobotPicoGo()
    #vitesse = 70
    #r2d2 = RobotTitan()
    #vitesse = 1 
    r2d2 = RobotGoliath()
    vitesse = 1
    #r2d2 = RobotPhil()
    #vitesse = 1
    #r2d2 = RobotBob()
    #vitesse = 1

    try:
        # avance pendant 0.5 secondes
        r2d2.moteur("gauche","avant",vitesse)
        r2d2.moteur("droit","avant",vitesse)
        time.sleep(0.5)
        r2d2.moteur("gauche","stop",1)
        r2d2.moteur("droit","stop",1)
        time.sleep(0.5)
        
        for loop in range(10):
            # tourne à droite
            r2d2.moteur("droit","avant",vitesse)
            time.sleep(0.2)
            r2d2.moteur("droit","stop",vitesse)
            time.sleep(1)

    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')
        r2d2.moteur("droit","stop",1)
        r2d2.moteur("gauche","stop",1)

if __name__ == '__main__':
    main_exemple_deplacement_robot()