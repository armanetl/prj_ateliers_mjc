from robot_goliath import RobotGoliath

import time

def main_exemple():
    # declare le robot
    goliath = RobotGoliath()

    # avance pendant 0.5 secondes
    goliath.moteur("gauche","avant",1)
    goliath.moteur("droit","avant",1)
    time.sleep(0.5)
    goliath.moteur("gauche","stop",1)
    goliath.moteur("droit","stop",1)
    time.sleep(0.5)
    
    for loop in range(10):
        # prend la mesure de distance
        m_cm = goliath.distance_cm("avant")
        print(f"mesure {m_cm} cm")
        # tourne à droite
        goliath.moteur("droit","avant",1)
        time.sleep(0.2)
        goliath.moteur("droit","stop",1)
        time.sleep(1)
        

if __name__ == '__main__':
    main_exemple()