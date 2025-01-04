from robot_phil import RobotPhil
import time

def main_exemple():
    # declare le robot
    phil = RobotPhil()

    # avance pendant 0.5 secondes
    phil.moteur("gauche","avant",1)
    phil.moteur("droit","avant",1)
    time.sleep(0.5)
    phil.moteur("gauche","stop",1)
    phil.moteur("droit","stop",1)
    time.sleep(0.5)
    
    for loop in range(10):
        # prend la mesure de distance
        m_cm = phil.distance_cm("avant")
        print(f"mesure {m_cm} cm")
        # tourne à droite
        phil.moteur("droit","avant",1)
        time.sleep(0.2)
        phil.moteur("droit","stop",1)
        time.sleep(1)
        

if __name__ == '__main__':
    main_exemple()