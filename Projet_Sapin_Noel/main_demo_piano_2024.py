#=====================================================
# Demo Piano :
# - Les 4 touches correspondent a des notes de musique
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
bouton1 = Pin(14, Pin.IN, Pin.PULL_UP)
bouton2 = Pin(15, Pin.IN, Pin.PULL_UP)
bouton3 = Pin(17, Pin.IN, Pin.PULL_UP)
bouton4 = Pin(18, Pin.IN, Pin.PULL_UP)
bouton5 = Pin(19, Pin.IN, Pin.PULL_UP)
bouton6 = Pin(20, Pin.IN, Pin.PULL_UP)
bouton7 = Pin(21, Pin.IN, Pin.PULL_UP)
bouton8 = Pin(22, Pin.IN, Pin.PULL_UP)

# Declaration des leds
# Declaration des leds
led1 = Pin(6, Pin.OUT)
led2 = Pin(7, Pin.OUT)
led3 = Pin(8, Pin.OUT)
led4 = Pin(9, Pin.OUT)
led5 = Pin(10, Pin.OUT)
led6 = Pin(11, Pin.OUT)
led7 = Pin(12, Pin.OUT)
led8 = Pin(13, Pin.OUT)

# Variables
bouton1_date_dernier_appui = time.ticks_ms()
bouton2_date_dernier_appui = time.ticks_ms()
bouton3_date_dernier_appui = time.ticks_ms()
bouton4_date_dernier_appui = time.ticks_ms()
bouton5_date_dernier_appui = time.ticks_ms()
bouton6_date_dernier_appui = time.ticks_ms()
bouton7_date_dernier_appui = time.ticks_ms()
bouton8_date_dernier_appui = time.ticks_ms()

bouton1_actif = False
bouton2_actif = False
bouton3_actif = False
bouton4_actif = False
bouton5_actif = False
bouton6_actif = False
bouton7_actif = False
bouton8_actif = False

# Fonction sera appellée lors de l'appui sur le bouton1
def bouton_handler(pin):
    global bouton1_actif, bouton2_actif, bouton3_actif, bouton4_actif
    global bouton5_actif, bouton6_actif, bouton7_actif, bouton8_actif
    global bouton1_date_dernier_appui, bouton2_date_dernier_appui, bouton3_date_dernier_appui, bouton4_date_dernier_appui
    global bouton5_date_dernier_appui, bouton6_date_dernier_appui, bouton7_date_dernier_appui, bouton8_date_dernier_appui
    if (pin == bouton1):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton1_date_dernier_appui) > 500: 
            bouton1_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton1_date_dernier_appui = time.ticks_ms() 
    if (pin == bouton2):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton2_date_dernier_appui) > 500: 
            bouton2_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton2_date_dernier_appui = time.ticks_ms() 
    if (pin == bouton3):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton3_date_dernier_appui) > 500: 
            bouton3_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton3_date_dernier_appui = time.ticks_ms() 
    if (pin == bouton4):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton4_date_dernier_appui) > 500: 
            bouton4_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton4_date_dernier_appui = time.ticks_ms() 
    if (pin == bouton4):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton4_date_dernier_appui) > 500: 
            bouton4_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton4_date_dernier_appui = time.ticks_ms() 
    if (pin == bouton5):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton5_date_dernier_appui) > 500: 
            bouton5_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton5_date_dernier_appui = time.ticks_ms() 
    if (pin == bouton6):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton6_date_dernier_appui) > 500: 
            bouton6_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton6_date_dernier_appui = time.ticks_ms() 
    if (pin == bouton7):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton7_date_dernier_appui) > 500: 
            bouton7_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton7_date_dernier_appui = time.ticks_ms() 
    if (pin == bouton8):
        # on evite les rebonds ...
        if time.ticks_diff(time.ticks_ms(), bouton8_date_dernier_appui) > 500: 
            bouton8_actif = True
            # on reinitialise la variable bouton_date_dernier_appui
            bouton8_date_dernier_appui = time.ticks_ms() 

# Fonction qui associe l'appui sur le bouton1 a l'appel de la fonction ci dessus
bouton1.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton2.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton3.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton4.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton5.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton6.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton7.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton8.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)

#Eteindre toutes les leds
led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)
led7.value(0)
led8.value(0)

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
    
# Boucle principale
while True:
    # on attends 1ms
    time.sleep(0.1)
    # on regarde l'etat du bouton1
    if bouton1_actif:
        print("bouton1 actif")
        joue_note("do_3")
        led1.toggle()
        bouton1_actif = False
    if bouton2_actif:
        print("bouton2 actif")
        joue_note("re_3")
        led2.toggle()
        bouton2_actif = False
    if bouton3_actif:
        print("bouton3 actif")
        joue_note("mi_3")
        led3.toggle()
        bouton3_actif = False
    if bouton4_actif:
        print("bouton4 actif")
        joue_note("fa_3")
        led4.toggle()
        bouton4_actif = False        
    if bouton5_actif:
        print("bouton5 actif")
        joue_note("sol_3")
        led5.toggle()
        bouton5_actif = False
    if bouton6_actif:
        print("bouton6 actif")
        joue_note("la_3")
        led6.toggle()
        bouton6_actif = False
    if bouton7_actif:
        print("bouton7 actif")
        joue_note("si_3")
        led7.toggle()
        bouton7_actif = False
    if bouton8_actif:
        print("bouton8 actif")
        led8.toggle()
        bouton8_actif = False         
