from robot_titan import RobotTitan
from mqtt import Mqtt
import time


def main_leonel():
    mqtt = Mqtt("titanLeonel")
    # declare le robot
    titan = RobotTitan()
    
    mqtt.publish("message", "titan demarre") 

    while True:
        titan.moteur("droit","avant", 1)
        time.sleep(1)
        titan.moteur("droit","stop", 1)
        distance = titan.distance_cm("avant")
        mqtt.publish("distance", "{0:2.2f}".format(distance)) 
        if distance < 10:
            break
        
    mqtt.publish("message", "titan a trouve la cible !!")
    
    

if __name__ == '__main__':
    main_leonel()
