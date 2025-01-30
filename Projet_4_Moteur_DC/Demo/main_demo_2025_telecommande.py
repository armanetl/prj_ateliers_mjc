from machine import Pin, PWM
from ir_rx_nec import NEC_16
from neopixel import Neopixel
import time

# declaration du ruban de leds (Pin 0)
NUM_LED = 8
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)
couleur_noir = (0,0,0)
couleurs = [couleur_vert,(0,200,0),(0,150,0),(50,100,0),(100,50,0),(150,0,0),(200,0,0),couleur_rouge]
leds.brightness(15)
leds.clear()
leds.show()

'''
# Moteur 1 : Voiture téléguidée
in1 = Pin(16,Pin.OUT,Pin.PULL_DOWN)
in2 = Pin(17,Pin.OUT,Pin.PULL_DOWN)
pwm = PWM(Pin(15))
min_duty= 18000
max_duty= 22000#30000

'''
# Moteur 2 : Moteur achat
in1 = Pin(20,Pin.OUT,Pin.PULL_DOWN)
in2 = Pin(19,Pin.OUT,Pin.PULL_DOWN)
pwm = PWM(Pin(18))
min_duty= 12000
max_duty= 20000#30000

# On stoppe le moteur
pwm.freq(1000)
pwm.duty_u16(0)
in1.value(1)
in2.value(1)

#Declaration et initialisation de variables internes
data_received = False
IR_data = 0

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

#Fonctions utiles pour declarer la telecommande 
def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        
ir = NEC_16(Pin(1, Pin.IN), callback)



#Boucle principale:
#Récupere le code reçu et selon sa valeur effectue une action
duty = 0
while True:
    if data_received:
        #print('Data 0x{:02x}'.format(IR_data))
        if (IR_data == Touche_0):
            duty = 0
            print('Touche 0: stop')
            in1.value(1)
            in2.value(1)
            pwm.duty_u16(duty)
            leds.clear()
            leds.show()

            time.sleep(1)

        elif (IR_data == Touche_1):
            duty = min_duty
            print('Touche 1: vitesse = ', duty)
            in1.value(0)
            in2.value(1)
            pwm.duty_u16(duty)
            for i in range (1):
                leds.set_pixel(i,couleurs[i])
            leds.show()
            time.sleep(1)

        elif (IR_data == Touche_2):
            duty = min_duty + 1000
            print('Touche 2: vitesse = ', duty)
            in1.value(0)
            in2.value(1)
            pwm.duty_u16(duty)
            for i in range (2):
                leds.set_pixel(i,couleurs[i])
            leds.show()
            time.sleep(1)
            
        elif (IR_data == Touche_3):
            duty = min_duty + 2*1000
            print('Touche 3: vitesse = ', duty)
            in1.value(0)
            in2.value(1)
            pwm.duty_u16(duty)
            for i in range (3):
                leds.set_pixel(i,couleurs[i])
            leds.show()
            time.sleep(1)

        elif (IR_data == Touche_4):
            duty = min_duty + 4*1000
            print('Touche 4: vitesse = ', duty)
            in1.value(0)
            in2.value(1)
            pwm.duty_u16(duty)
            for i in range (4): #0,1,2,3
                leds.set_pixel(i,couleurs[i])
            leds.show()
            time.sleep(1)

        else:
            print('Touche non programmée')
        
        data_received = False


