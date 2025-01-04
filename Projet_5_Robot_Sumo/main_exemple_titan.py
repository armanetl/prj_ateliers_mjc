from robot_titan import RobotTitan
import time

def main_exemple():
    # declare le robot
    titan = RobotTitan()

    # avance pendant 0.5 secondes
    titan.moteur("gauche","avant",1)
    titan.moteur("droit","avant",1)
    time.sleep(0.5)
    titan.moteur("gauche","stop",1)
    titan.moteur("droit","stop",1)
    time.sleep(0.5)
    
    for loop in range(10):
        # prend la mesure de distance
        m_cm = titan.distance_cm("avant")
        print(f"mesure {m_cm} cm")
        # tourne à droite
        titan.moteur("droit","avant",1)
        time.sleep(0.2)
        titan.moteur("droit","stop",1)
        time.sleep(1)
        

if __name__ == '__main__':
    main_exemple()