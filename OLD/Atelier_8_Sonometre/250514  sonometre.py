from machine import Pin, ADC #import des différentes classes pour fonctionner
from neopixel import Neopixel
import utime, time

leds = Neopixel(8,0,16,"GRB") #initialisation de la bande de leds
leds.brightness(20) # initialisation de la luminosité des leds
mic = ADC(26)# initialisation de l'entrée analogique
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
lut = [(64543,8),(60235,7),(56215,6),(52463,5),(48961,4),(45693,3),(42643,2),(39796,1),(37141,0)]

if __name__ == '__main__':
    print("Start")
    max_led = 0 #initialisation de la variable à 0
    start_time = utime.ticks_ms() #enregistre le temps de démarrage

    leds.set_pixel_line_gradient(0,7,(255,0,0),(0,255,0)) #initialisation des leds du vert au rouge
    leds.show()
    time.sleep (1) # durée 1 seconde
    while True: # boucle principale
        ve = mic.read_u16() # lecture de la tension du micro-electret
        time.sleep (0.01) # tempo de 0.01s
        print(ve) # impression de la valeur numérique lue
        
        for item in lut:   #pour chaque seuil, comparaison avec ve          
            if ve > item[0]:   # item[0] c'est pour chaque tulpe la valeur du seuil             
                # on prepare le gradient de couleur sur toute les leds
                leds.set_pixel_line_gradient(0,7,(0,255,0),(255,0,0))
                # on efface les leds supérieures à la led que l'on a trouvée
                leds.set_pixel_line(item[1],7,(0,0,0)) # item[1], c'est le N° de la led, (0,0,0) c'est la couleur noire
                # on regarde si cette nouvelle led est plus grande que la derniere plus grande valeur trouvee
                if max_led < item[1]: # c'est pour sélectionner la led correspondant au seuil max et la mettre en bleu
                    max_led = item[1]
                    # test pour etre sur de ne pas depasser le nombre de led
                    if max_led > 7:
                        max_led = 7
                # affiche en bleu la led la plus haute des 1.5 dernière secondes
                leds.set_pixel(max_led,(0,0,255))
                # affiche le cumul des opérations de définition des leds ci-dessus
                leds.show()
                # réinitialisation de la position de la led Bleue toutes les 1.5s
                if (utime.ticks_ms()-start_time) > 1500:
                    max_led = 0
                    start_time += 1500
                
                break # sort de la boucle pour recommencer une lecture de la tension du micro-electret

    print("Stop")