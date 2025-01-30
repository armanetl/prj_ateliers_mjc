from machine import ADC
import time
import utime

#r2d2_name = "PicoGo"
r2d2_name = "Yaboom"

if (r2d2_name == "PicoGo"):
    from robot_picogo import RobotPicoGo
    r2d2 = RobotPicoGo()
    couleur_vert = r2d2.oled.GREEN
    couleur_bleu = r2d2.oled.BLUE
    couleur_noir = r2d2.oled.BLACK
elif (r2d2_name == "Yaboom"):
    from robot_yaboom import RobotYaboom
    r2d2 = RobotYaboom()
    couleur_vert = 0xFFFF #Blanc
    couleur_bleu = 0xFFFF #Blanc
    couleur_noir = 0x0000 #Noir

def main_exemple_oled():

    global r2d2

    temp = ADC(4)
 
    r2d2.oled.fill(couleur_noir)
    r2d2.oled.text('Hello', 0, 0,couleur_vert)
    r2d2.oled.show()
    time.sleep(1)

    try:
        while True:
            utime.sleep(1)
            reading = temp.read_u16() * 3.3 / (65535)
            temperature = 27 - (reading - 0.706)/0.001721

            r2d2.oled.fill(couleur_noir)
            r2d2.oled.text("temp: {:5.2f} C".format(temperature),0,20,couleur_bleu)

            r2d2.oled.show()
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')


if __name__ == '__main__':
    main_exemple_oled()