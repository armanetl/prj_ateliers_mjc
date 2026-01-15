from machine import Pin, ADC, I2C
import utime, time
from buzzer import Buzzer
import math
import random
from ssd1306 import SSD1306_I2C


#Initialisation des leds

led_0 = Pin(19, Pin.OUT)
led_1 = Pin(18, Pin.OUT)
led_2 = Pin(17, Pin.OUT)
led_3 = Pin(16, Pin.OUT)

led_10 = Pin(26, Pin.OUT)
led_11 = Pin(22, Pin.OUT)
led_12 = Pin(21, Pin.OUT)
led_13 = Pin(20, Pin.OUT)


buz = Buzzer(13)

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=100000)
#i2c=I2C(1,sda=Pin(18), scl=Pin(19), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)

mic = ADC(28)# initialisation de l'entrée analogique
# le préamplificateur positionne la tension moyenne à 1.65V pour avoir une sinusoide du signal complète avec la partie négative du signal.
# donc on a une plage de tension de 1.65 à 3.3V
# table de conversion des seuils (volts) en valeur numériques: mic*65536(16bits)/3,3(tension d'alim du micro-electret)
# la valeur maximale lue est definie à 3.25V donc en numerique 64543
# calcul des seuils, -0.3dB d'écart avec seuil de 64543 est = 64543*10puissance(-0.3/10)
# led 8 = 65543 (qui n'esiste pas, mais on a besoin de ce seuil)
# led 7 -0.3dB de 65543= 60235
# led 6 -0.6dB = 56215
# led 5 -0.9dB = 52463
# led 4 -1.2dB = 48961
# led 3 -1.5dB = 45693
# led 2 -1.8dB = 42643
# led 1 - 2.1 dB = 39796
# led 0 -2.4 dB = 37141
# la diminution de 0.3 dB en tension correspond à 6.7% de réduction de puissance
# la diminution de 0.46 dB en tension correspond à 10% de réduction de puissance
# la diminution de 3 dB en tension correspond à 50% de réduction de puissance
# lut = liste de seuils et de N° de led ( seuil, numero de led) = Tulpe
#lut = [(64543,8),(60235,7),(56215,6),(52463,5),(48961,4),(45693,3),(42643,2),(39796,1),(37141,0)]
lut = [(52463,3),(42643,2),(37141,1),(30141,0)]

#Eteindre toutes les leds
led_0.value(0)
led_1.value(0)
led_2.value(0)
led_3.value(0)
led_10.value(0)
led_11.value(0)
led_12.value(0)
led_13.value(0)

def beep():
    global buz
    buz.set_volume(12000)
    buz.set_freq(1046)
    buz.start()
    time.sleep(1)
    buz.stop()      

#Dimensions OLED SSD1306
x_oeil_1 = 20
x_oeil_2 = 70
largeur_oeil = 40
y_oeil = 10
hauteur_oeil = 10

CODE_NOIR = 0
CODE_COULEUR = 10

CODE_TAILLE_MIN = 0
CODE_TAILLE_MAX = 10

TICK=0

def displayTick():
    oled.show()
    time.sleep(TICK)
    
#Fonctions qui gèrent un oeil => effacer les lignes non utilisées ?
def oeil(x,taille):
    #Protection
    if taille < CODE_TAILLE_MIN:
        taille = CODE_TAILLE_MIN
    if taille == CODE_TAILLE_MIN:
        for i in range(y_oeil,y_oeil + hauteur_oeil):
            oled.hline(x,i,largeur_oeil,CODE_NOIR)
    else:
        #Protection
        if taille > CODE_TAILLE_MAX:
            taille = CODE_TAILLE_MAX
        debut = y_oeil - taille
        for i in range(y_oeil + debut,y_oeil + hauteur_oeil):
            oled.hline(x,i,largeur_oeil,CODE_COULEUR)

def oeil_biais(x):
    oled.hline(x,13,largeur_oeil-32,CODE_COULEUR)
    oled.hline(x,14,largeur_oeil-24,CODE_COULEUR)
    oled.hline(x,15,largeur_oeil-16,CODE_COULEUR)
    oled.hline(x,16,largeur_oeil-8,CODE_COULEUR)
    for i in range(17,20):
        oled.hline(x,i,largeur_oeil,CODE_COULEUR)

def oeil_biais_2(x):
    oled.hline(x+32,13,largeur_oeil-32,CODE_COULEUR)
    oled.hline(x+24,14,largeur_oeil-24,CODE_COULEUR)
    oled.hline(x+16,15,largeur_oeil-16,CODE_COULEUR)
    oled.hline(x+8,16,largeur_oeil-8,CODE_COULEUR)
    for i in range(17,20):
        oled.hline(x,i,largeur_oeil,CODE_COULEUR)

#Fonctions qui gèrent les yeux
#=============================
def oled_clean():
    oeil(x_oeil_1,CODE_TAILLE_MIN)
    oeil(x_oeil_2,CODE_TAILLE_MIN)
    oled.show()
    #time.sleep(0.05)
    
def yeux_taille(taille):
    #oled_clean()
    oeil(x_oeil_1,taille)
    oeil(x_oeil_2,taille)
    displayTick()    

def colere():
    oled_clean()
    oeil_biais(x_oeil_1)
    oeil_biais_2(x_oeil_2)
    displayTick()

if __name__ == '__main__':
    print("Start")

    while True: # boucle principale
        ve = mic.read_u16() # lecture de la tension du micro-electret
        #print(ve)
        time.sleep (0.04) # tempo de 0.01s
        yeux_taille(10)

        
        for (seuil,niveau) in lut:   #pour chaque seuil, comparaison avec ve          
            if ve > seuil:              
                print(niveau)
                if niveau >= 0:
                    led_0.value(1)
                    led_10.value(1)
                else:
                    led_0.value(0)
                    led_10.value(0)
                if niveau >= 1:
                    led_1.value(1)
                    led_11.value(1)
                else:
                    led_1.value(0)
                    led_11.value(0)  
                if niveau >= 2:
                    led_2.value(1)
                    led_12.value(1)
                else:
                    led_2.value(0)
                    led_12.value(0)  
                if niveau >= 3:
                    led_3.value(1)
                    led_13.value(1)
                    colere()
                    beep()
                else:
                    led_3.value(0)
                    led_13.value(0) 
                break # sort de la boucle pour recommencer une lecture de la tension du micro-electret


