import time

#r2d2_name = "PicoGo"
r2d2_name = "Yaboom"
#r2d2_name = "Titan"

if (r2d2_name == "PicoGo"):
    from robot_picogo import RobotPicoGo
    r2d2 = RobotPicoGo()
elif (r2d2_name == "Yaboom"):
    from robot_yaboom import RobotYaboom
    r2d2 = RobotYaboom()
elif (r2d2_name == "Titan"):
    from robot_titan import RobotTitan
    r2d2 = RobotTitan()


def main_exemple_neopixel():

    global r2d2
  
    r2d2.leds.brightness(15)
    r2d2.leds.clear()
    r2d2.leds.show()
    
    try:
        while True:
            # on allume toutes les leds du sapin en rouge
            #leds.fill((255,0,0))
            r2d2.leds.fill((255,0,0))
            r2d2.leds.show()
            time.sleep(1)
            # on allume toutes les leds du sapin en vert
            r2d2.leds.fill((0,255,0))
            r2d2.leds.show()
            time.sleep(1)
            # on allume toutes les leds du sapin en bleu
            r2d2.leds.fill((0,0,255))
            r2d2.leds.show()
            time.sleep(1)
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')


if __name__ == '__main__':
    main_exemple_neopixel()