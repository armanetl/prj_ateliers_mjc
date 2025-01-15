#from robot_yaboom import RobotYaboom
#from robot_picogo import RobotPicoGo
from robot_titan import RobotTitan
#from robot_goliath import RobotGoliath
#from robot_phil import RobotPhil
#from robot_bob import RobotBob
from ir_rx_nec import NEC_16
from machine import Pin
import time

#Fonctions utiles pour declarer la telecommande 
def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        
ir = NEC_16(Pin(5, Pin.IN), callback)

#Declaration et initialisation de variables internes
data_received = False
IR_data = 0

def main_exemple_telecommande_titan():

    # declare le robot
    #r2d2 = RobotYaboom()
    #vitesse = 70
    #r2d2 = RobotPicoGo()
    #vitesse = 70
    r2d2 = RobotTitan()
    vitesse = 1 
    #r2d2 = RobotGoliath()
    #vitesse = 1
    #r2d2 = RobotPhil()
    #vitesse = 1
    #r2d2 = RobotBob()
    #vitesse = 1

    global data_received,IR_data

    #Definition du code de chaque touche en fonction de la telecommande utilisée
    '''
    Touche_0 = 0x19
    Touche_1 = 0x45
    Touche_2 = 0x46
    Touche_3 = 0x47
    Touche_4 = 0x44
    Touche_5 = 0x40
    Touche_6 = 0x43
    Touche_7 = 0x07
    Touche_8 = 0x15
    Touche_9 = 0x09
    '''
    Touche_H = 0x18
    Touche_D = 0x5A
    Touche_B = 0x52
    Touche_G = 0x08
    Touhe_OK = 0x1C
    

    try:
        while True:
            if data_received:
                print('Data 0x{:02x}'.format(IR_data))
                if (IR_data == Touche_H):
                    print('Touche H: on avance')
                    r2d2.moteur("gauche","avant",vitesse)
                    r2d2.moteur("droit","avant",vitesse)
                    time.sleep(0.5)
                    r2d2.moteur("gauche","stop",1)
                    r2d2.moteur("droit","stop",1)
                    time.sleep(0.5)

                elif (IR_data == Touche_B):
                    print('Touche B: on recule')
                    r2d2.moteur("gauche","arriere",vitesse)
                    r2d2.moteur("droit","arriere",vitesse)
                    time.sleep(0.5)
                    r2d2.moteur("gauche","stop",1)
                    r2d2.moteur("droit","stop",1)
                    time.sleep(0.5)                       

                elif (IR_data == Touche_D):
                    print('Touche D: on tourne a droite')
                    r2d2.moteur("gauche","avant",vitesse)
                    r2d2.moteur("droit","arriere",vitesse)
                    time.sleep(0.5)
                    r2d2.moteur("gauche","stop",1)
                    r2d2.moteur("droit","stop",1)
                    time.sleep(0.5)                       
                    
                elif (IR_data == Touche_G):
                    print('Touche G: on tourne a droite')
                    r2d2.moteur("gauche","arriere",vitesse)
                    r2d2.moteur("droit","avant",vitesse)
                    time.sleep(0.5)
                    r2d2.moteur("gauche","stop",1)
                    r2d2.moteur("droit","stop",1)
                    time.sleep(0.5)                       
                    
                else:
                    print('Touche non programmée')
                data_received = False
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')
        r2d2.moteur("droit","stop",1)
        r2d2.moteur("gauche","stop",1)

if __name__ == '__main__':
    main_exemple_telecommande_titan()