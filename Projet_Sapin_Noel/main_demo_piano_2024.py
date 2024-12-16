#=====================================================
# Demo Piano :
# - Les boutons correspondent a des notes de musique
# clair_lune = [("fa_3",N), ("fa_3",N), ("fa_3",N), ("sol_3",N),
#               ("la_3",B), ("sol_3",B),
#               ("fa_3",N), ("la_3",N), ("sol_3",N), ("sol_3",N),
#               ("fa_3",R),
#               ("fa_3",N), ("fa_3",N), ("fa_3",N), ("sol_3",N),
#               ("la_3",B), ("sol_3",B),
#               ("fa_3",N), ("la_3",N), ("sol_3",N), ("sol_3",N),
#               ("fa_3",R)]
#=====================================================
from machine import Pin
from buzzer import Buzzer
from time import sleep
import time

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

# frequence note
freq_notes = {"do_2":130.81,"do#_2":138.59,
              "re_2":146.83,"re#_2":155.56,
              "mi_2":164.81,
              "fa_2":174.61,"fa#_2":185.00,
              "sol_2":196,"sol#_2":207.65,
              "la_2":220,"la#_2":233.08,
              "si_2":246.94,
              "do_3":261.63,"do#_3":277.18,
              "re_3":293.66,"re#_3":311.13,
              "mi_3":329.63,
              "fa_3":349.23,"fa#_3":369.99,
              "sol_3":392,"sol#_3":415.30,
              "la_3":440,"la#_3":466.16,
              "si_3":493.88,
              "do_4":523.25,"do#_4":554.37,
              "re_4":587.33,"re#_4":622.25,
              "mi_4":659.26,
              "fa_4":698.46,"fa#_4":739.99,
              "sol_4":783.99,"sol#_4":830.61,
              "la_4":880,"la#_4":932.33,
              "si_4":987.77,
              "do_5":1046.50,"do#_5":1108.73,
              "re_5":1174.66,"re#_5":1244.51,
              "mi_5":1318.51,
              "fa_5":1396.91,"fa#_5":1479.98,
              "sol_5":1567.98,"sol#_5":1661.22,
              "la_5":1760.00,"la#_5":1864.66,
              "si_5":1967.53}

#
buz = Buzzer(2)
buz.stop()

#
def joue_note(val_note):
    global buz
    buz.set_freq(freq_notes[val_note])
    buz.start()
    sleep(0.2)
    buz.stop()

notes = ["do_3","re_3","mi_3","fa_3","sol_3","la_3","si_3"]
# Boucle principale
while True:
    # on attends
    time.sleep(0.2)
    # on regarde l'etat des boutons
    for i in range(8):
        if boutons_actif[i]:
            print("bouton " + str(i) + " actif")
            joue_note(notes[i])
            leds[i].toggle()
            boutons_actif[i] = False

