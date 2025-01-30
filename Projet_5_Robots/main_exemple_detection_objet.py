import time

#r2d2_name = "PicoGo"
#r2d2_name = "Yaboom"
#r2d2_name = "Titan"
#r2d2_name = "Goliath"
r2d2_name = "Bob"
#r2d2_name = "Phil"

if (r2d2_name == "PicoGo"):
    from robot_picogo import RobotPicoGo
    r2d2 = RobotPicoGo()
elif (r2d2_name == "Yaboom"):
    from robot_yaboom import RobotYaboom
    r2d2 = RobotYaboom()
elif (r2d2_name == "Titan"):
    from robot_titan import RobotTitan
    r2d2 = RobotTitan()
elif (r2d2_name == "Goliath"):
    from robot_goliath import RobotGoliath
    r2d2 = RobotGoliath()
elif (r2d2_name == "Bob"):
    from robot_bob import RobotBob
    r2d2 = RobotBob()
elif (r2d2_name == "Phil"):
    from robot_phil import RobotPhil
    r2d2 = RobotPhil()

def main_exemple_detection_objet():

    global r2d2

    vitesse = r2d2.vitesse_moyenne

    try:
        while True:
            distance = r2d2.distance_cm("avant")
            print('Distance:', "{0:2.2f}".format(distance), 'cm')
            if (distance > 20):
                #Moteur tourne a gauche
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