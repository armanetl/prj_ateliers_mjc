from ir_rx_nec import NEC_16
from machine import Pin
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

#Fonctions utiles pour declarer la telecommande 
def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        

#Declaration et initialisation de variables internes
data_received = False
IR_data = 0

def main_exemple_telecommande():

    global r2d2
    global data_received,IR_data

    vitesse = r2d2.vitesse_moyenne
    pin_telecommande = r2d2.pin_telecommande
    Touche_H = r2d2.Code_Touche_Haut
    Touche_D = r2d2.Code_Touche_Droite
    Touche_B = r2d2.Code_Touche_Bas
    Touche_G = r2d2.Code_Touche_Gauche

    ir = NEC_16(Pin(pin_telecommande, Pin.IN), callback)   

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
    main_exemple_telecommande()