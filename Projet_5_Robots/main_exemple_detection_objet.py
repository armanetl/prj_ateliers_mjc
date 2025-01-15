#from robot_yaboom import RobotYaboom
#from robot_picogo import RobotPicoGo
#from robot_titan import RobotTitan
#from robot_goliath import RobotGoliath
from robot_phil import RobotPhil
#from robot_bob import RobotBob
import time

def main_exemple_detection_objet():


    # declare le robot
    #r2d2 = RobotYaboom()
    #vitesse = 70
    #r2d2 = RobotPicoGo()
    #vitesse = 70
    #r2d2 = RobotTitan()
    #vitesse = 1 
    #r2d2 = RobotGoliath()
    #vitesse = 1
    r2d2 = RobotPhil()
    vitesse = 1
    #r2d2 = RobotBob()
    #vitesse = 1
    
    try:
        while True:
            distance = r2d2.distance_cm("avant")
            print('Distance:', "{0:2.2f}".format(distance), 'cm')
            if (distance > 20):
                #Moteur tourne
                print('RAS')
                r2d2.moteur("droit","avant",vitesse)
                r2d2.moteur("gauche","arriere",vitesse)
                time.sleep(0.6)
            else:
                #Moteur stop
                print('STOP !!!!!!!!!!!!!!!!')
                r2d2.moteur("droit","stop",1)
                r2d2.moteur("gauche","stop",1)
                time.sleep(5)#
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')
        r2d2.moteur("droit","stop",1)
        r2d2.moteur("gauche","stop",1)

if __name__ == '__main__':
    main_exemple_detection_objet()