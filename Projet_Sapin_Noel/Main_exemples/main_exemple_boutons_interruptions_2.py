#=====================================================
# Main Exemple Boutons & Interruptions:
# - Un appui sur les boutons déclenche une interruption
# - Le CPU execute un handler (= routine d'interruption)
#   qui va setter une variable 
#=====================================================
# Imports
from machine import Pin
import time

# Declaration
bouton1 = Pin(14, Pin.IN, Pin.PULL_UP)
bouton2 = Pin(15, Pin.IN, Pin.PULL_UP)
bouton3 = Pin(17, Pin.IN, Pin.PULL_UP)
bouton4 = Pin(18, Pin.IN, Pin.PULL_UP)
bouton5 = Pin(19, Pin.IN, Pin.PULL_UP)
bouton6 = Pin(20, Pin.IN, Pin.PULL_UP)
bouton7 = Pin(21, Pin.IN, Pin.PULL_UP)
bouton8 = Pin(22, Pin.IN, Pin.PULL_UP)

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

# Boucle principale
while True:
    # on attends 
    time.sleep(0.2)
    # on regarde l'etat des boutons
    if bouton1_actif:
        print("bouton1 actif")
        bouton1_actif = False
    if bouton2_actif:
        print("bouton2 actif")
        bouton2_actif = False
    if bouton3_actif:
        print("bouton3 actif")
        bouton3_actif = False
    if bouton4_actif:
        print("bouton4 actif")
        bouton4_actif = False
    if bouton5_actif:
        print("bouton5 actif")
        bouton5_actif = False
    if bouton6_actif:
        print("bouton6 actif")
        bouton6_actif = False
    if bouton7_actif:
        print("bouton7 actif")
        bouton7_actif = False
    if bouton8_actif:
        print("bouton8 actif")
        bouton8_actif = False

