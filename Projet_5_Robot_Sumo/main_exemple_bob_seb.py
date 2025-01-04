from robot_bob import RobotBob
import time

def main_seb():
    # declare le robot
    bob = RobotBob()

    # avance pendant 0.5 secondes
    bob.moteur("gauche","avant",1)
    bob.moteur("droit","avant",1)
    time.sleep(0.5)
    bob.moteur("gauche","stop",1)
    bob.moteur("droit","stop",1)
    
    for loop in range(10):
        # prend la mesure de distance
        m_cm = bob.distance_cm("avant")
        print(f"mesure {m_cm} cm")
        # tourne à droite
        bob.moteur("droit","avant",1)
        time.sleep(0.2)
        bob.moteur("droit","stop",1)
        
