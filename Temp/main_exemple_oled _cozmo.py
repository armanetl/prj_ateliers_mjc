from classe_cozmo_eyes import Cozmo_Eyes

r2d2_name = "PicoGo"
#r2d2_name = "Yaboom"

if (r2d2_name == "PicoGo"):
    from robot_picogo import RobotPicoGo
    r2d2 = RobotPicoGo()
elif (r2d2_name == "Yaboom"):
    from robot_yaboom import RobotYaboom
    r2d2 = RobotYaboom()

def main_exemple_oled_cozmo():

    global r2d2
 
    cozmo = Cozmo_Eyes(r2d2.oled,r2d2.oled_width,r2d2.oled_height,r2d2.oled_color)

    try:
        while True:
            #Normal
            cozmo.yeux_taille(10)
            cozmo.yeux_taille(5)
            cozmo.yeux_taille(10)
            cozmo.clin_oeil_droit()
            cozmo.yeux_taille(10)
            cozmo.clin_oeil_gauche()
            cozmo.yeux_taille(10)
            cozmo.yeux_taille(2)
            cozmo.yeux_taille(10)
            cozmo.colere()
            cozmo.depite()

    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')

if __name__ == '__main__':
    main_exemple_oled_cozmo()