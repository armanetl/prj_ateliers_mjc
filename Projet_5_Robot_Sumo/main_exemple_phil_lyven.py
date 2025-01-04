from robot_phil import RobotPhil
#from mqtt import Mqtt
import time

def main_lyven():
    # declare le robot
    phil = RobotPhil()
    # declare MQTT
    #mqtt = Mqtt('phil')

    # avance pendant 0.5 secondes
    #phil.moteur("gauche","avant",1)
    #phil.moteur("droit","avant",1)
    #time.sleep(0.5)
    #phil.moteur("gauche","stop",1)
    #phil.moteur("droit","stop",1)
    #time.sleep(0.5)
    
    #for loop in range(10):
    while True:
        #tourne
        phil.moteur("droit","avant",1)
        phil.moteur("gauche","recule",1)
        #delais
        time.sleep(1)
        #stop
        phil.moteur("gauche","stop",1)
        phil.moteur("droit","stop",1)
        # prend la mesure de distance
        m_cm = phil.distance_cm("avant")
        print(f"mesure {m_cm} cm")
        #test
        if (m_cm<10):
            break
        
    phil.moteur("gauche","stop",1)
    phil.moteur("droit","stop",1)
    print(f"cible trouvee !!!")
    #on fonce dessut!!!!
    phil.moteur("droit","avant",1)
    phil.moteur("gauche","avance",1)
    
    
    
if __name__ == '__main__':
    main_lyven()
    