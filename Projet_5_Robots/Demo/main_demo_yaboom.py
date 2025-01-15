from robot_yaboom import RobotYaboom
from machine import Pin, I2C, ADC
from pico_car_mjc import SSD1306_I2C
import time

def main_demo():
    # declare le robot
    yoyo = RobotYaboom()
    
    #initialization oled
    i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
    oled = SSD1306_I2C(128, 32, i2c)
    #initialization ADC
    Quantity_of_electricity = ADC(28)    

    try:
        while True:
            #Display power on OLED,Under 20000, there is no power at all
            oled.text('Power:', 0, 0)
            oled.text(str(Quantity_of_electricity.read_u16()), 45, 0)
            if (Quantity_of_electricity.read_u16() < 25000):
                oled.text('LOW', 100, 0)
            else:
                oled.text('OK', 100, 0)         
            oled.show()
            oled.fill(0)
            time.sleep(0.1)
            distance = yoyo.distance_cm("avant")
            print('Distance:', "{0:2.2f}".format(distance), 'cm')
            oled.text('Distance:', 0, 10)
            oled.text(str(distance), 80, 10)
            if (distance > 20):
                #Moteur tourne
                print('RAS')                
                oled.text('RAS', 0, 20)
                yoyo.moteur("droit","avant",60)
                yoyo.moteur("gauche","arriere",60)
                time.sleep(0.6)
            else:
                #Moteur stop
                print('STOP !!!!!!!!!!!!!!!!')
                oled.text('STOP!!!!!', 0, 20)
                oled.show()
                oled.fill(0)
                yoyo.moteur("droit","stop",1)
                yoyo.moteur("gauche","stop",1)
                time.sleep(1)
                print('FONCE !!!!!!!!!!!!!!!!')
                oled.text('FONCE!!!!!', 0, 20)
                oled.show()
                oled.fill(0)
                yoyo.moteur("droit","avant",60)
                yoyo.moteur("gauche","avant",60)
                time.sleep(0.6)
                
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')
        yoyo.moteur("droit","stop",1)
        yoyo.moteur("gauche","stop",1)

if __name__ == '__main__':
    main_demo()