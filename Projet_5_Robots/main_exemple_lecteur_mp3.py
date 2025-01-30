from dfplayermini import Player
from machine import Pin
import time

r2d2_name = "Yaboom"

if (r2d2_name == "Yaboom"):
    from robot_yaboom import RobotYaboom
    r2d2 = RobotYaboom()

def main_exemple_lecteur_mp3():

    global r2d2

    #UART0 (modif de la lib!) Tx,Rx
    music = Player(Pin(16), Pin(17))
    music.module_wake()
    music.volume(100)
    
    try:
        while True:
            music.play(1) 
            time.sleep(15)
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')

if __name__ == '__main__':
    main_exemple_lecteur_mp3()