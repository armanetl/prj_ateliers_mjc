from machine import Pin
from ir_rx_nec import NEC_16
from neopixel import Neopixel
import time

#Declaration et initialisation de variables internes
data_received = False
IR_data = 0

#Declaration du ruban de leds (Pin 0)
NUM_LED = 30
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")
leds.brightness(15)
leds.clear()
leds.show()

#Definition du code de chaque touche en fonction de la telecommande utilisée
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
Touche_H = 0x18
Touche_D = 0x5A
Touche_B = 0x52
Touche_G = 0x08
Touhe_OK = 0x1C

#Declaration de quelques couleurs 
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)
couleur_noir = (0,0,0)


#Fonctions utiles pour declarer la telecommande 
def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        
ir = NEC_16(Pin(3, Pin.IN), callback)

#Boucle principale:
#Récupere le code reçu et selon sa valeur effectue une action (ici simple printf)
while True:
    if data_received:
        #print('Data 0x{:02x}'.format(IR_data))
        if (IR_data == Touche_0):
            print('Touche 0: on allume toutes les leds du sapin en bleu')
            leds.fill(couleur_bleu)
            leds.show()
            time.sleep(1)

        elif (IR_data == Touche_1):
            print('Touche 1: on allume tour a tour  les leds du sapin en vert')
            for i in range (0,NUM_LED):
                leds.set_pixel(i,couleur_vert)
                leds.show()
                time.sleep(0.1)
            leds.clear()
            leds.show()                       

        elif (IR_data == Touche_2):
            print('Touche 2: on allume un bloc de leds')
            leds.set_pixel_line(5,20,couleur_rouge)
            leds.show()
            time.sleep(2)
            leds.clear()
            leds.show()
            
        elif (IR_data == Touche_3):
            print('Touche 3: on fait un gradient de couleur')
            leds.set_pixel_line_gradient(5,20,couleur_vert,couleur_bleu)
            leds.show()
            time.sleep(2)
            leds.clear()
            leds.show()

        elif (IR_data == Touche_4):
            print('Touche 4: rotation d un bloc de leds a droite')
            leds.set_pixel_line(0,3,couleur_bleu)
            for i in range (NUM_LED):
                leds.rotate_right(1)
                leds.show()
                time.sleep (0.2)
                i=i+1 
            leds.clear()
            leds.show()

        elif (IR_data == Touche_5):
            print('Touche 5: rotation d un bloc de leds a gauche')
            leds.set_pixel_line(0,3,couleur_vert)
            for i in range (NUM_LED):
                leds.rotate_left(1)
                leds.show()
                time.sleep (0.2)
                i=i+1 
            leds.clear()
            leds.show()
            
        else:
            print('Touche non programmée')
        data_received = False
