#=====================================================
# Demo Piano :
# - Les boutons correspondent a des notes de musique
#=====================================================
from machine import Pin
from buzzer import Buzzer
from classe_music_P import Music_P
from time import sleep
import time

# Declaration du buzzer et de la classe music
buz = Buzzer(2)
buz.stop()
music = Music_P(buz)

# Declaration des boutons
boutons = [Pin(14, Pin.IN, Pin.PULL_UP),Pin(15, Pin.IN, Pin.PULL_UP),
           Pin(17, Pin.IN, Pin.PULL_UP),Pin(18, Pin.IN, Pin.PULL_UP),
           Pin(19, Pin.IN, Pin.PULL_UP),Pin(20, Pin.IN, Pin.PULL_UP),
           Pin(21, Pin.IN, Pin.PULL_UP),Pin(22, Pin.IN, Pin.PULL_UP)]

# Declaration des leds
leds = [Pin(6, Pin.OUT),Pin(7, Pin.OUT),
        Pin(8, Pin.OUT),Pin(9, Pin.OUT),
        Pin(10, Pin.OUT),Pin(11, Pin.OUT),
        Pin(12, Pin.OUT),Pin(13, Pin.OUT)]

# Variables
boutons_date_dernier_appui = [time.ticks_ms(),time.ticks_ms(),
                              time.ticks_ms(),time.ticks_ms(),
                              time.ticks_ms(),time.ticks_ms(),
                              time.ticks_ms(),time.ticks_ms()]

boutons_actif = [False,False,False,False,False,False,False,False]

# Fonction sera appellée lors de l'appui sur le bouton1
def bouton_handler(pin):
    global boutons_actif
    global boutons_date_dernier_appui
    if (pin == boutons[0]):
        i = 0
    if (pin == boutons[1]):
        i = 1
    if (pin == boutons[2]):
        i = 2
    if (pin == boutons[3]):
        i = 3
    if (pin == boutons[4]):
        i = 4
    if (pin == boutons[5]):
        i = 5
    if (pin == boutons[6]):
        i = 6   
    if (pin == boutons[7]):
        i = 7
    # on evite les rebonds ...
    if time.ticks_diff(time.ticks_ms(), boutons_date_dernier_appui[i]) > 500: 
        boutons_actif[i] = True
        # on reinitialise la variable bouton_date_dernier_appui
        boutons_date_dernier_appui[i] = time.ticks_ms() 

# Fonction qui associe l'appui sur le bouton1 a l'appel de la fonction ci dessus
for bouton in boutons:
    bouton.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)

#Eteindre toutes les leds
for led in leds:
    led.value(0)

notes = ["do_3","re_3","mi_3","fa_3","sol_3","la_3","si_3"]

# Boucle principale
while True:
    # on attends
    time.sleep(0.2)
    # on regarde l'etat des boutons
    for i in range(8):
        if boutons_actif[i]:
            print("bouton " + str(i) + " actif")
            music.joue_note(notes[i],1)
            leds[i].toggle()
            boutons_actif[i] = False

