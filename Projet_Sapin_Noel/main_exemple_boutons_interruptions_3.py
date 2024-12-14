#=====================================================
# Main Exemple Boutons & Interruptions:
# - Un appui sur les 4boutons déclenche une interruption
# - Le CPU execute un handler (= routine d'interruption)
#   qui va setter une variable
# - On toggle des LEDs a chaque appui sur les boutons
#=====================================================
# Imports
from machine import Pin
import time

# Declaration des boutons
bouton1 = Pin(10, Pin.IN, Pin.PULL_UP)
bouton2 = Pin(11, Pin.IN, Pin.PULL_UP)
bouton3 = Pin(12, Pin.IN, Pin.PULL_UP)
bouton4 = Pin(13, Pin.IN, Pin.PULL_UP)

# Declaration des leds
led1 = Pin(6, Pin.OUT)
led2 = Pin(7, Pin.OUT)
led3 = Pin(8, Pin.OUT)
led4 = Pin(9, Pin.OUT)

# Variables
bouton1_date_dernier_appui = time.ticks_ms()
bouton2_date_dernier_appui = time.ticks_ms()
bouton3_date_dernier_appui = time.ticks_ms()
bouton4_date_dernier_appui = time.ticks_ms()
bouton1_actif = False
bouton2_actif = False
bouton3_actif = False
bouton4_actif = False

# Fonction sera appellée lors de l'appui sur le bouton1
def bouton_handler(pin):
    global bouton1_actif, bouton2_actif, bouton3_actif, bouton4_actif
    global bouton1_date_dernier_appui, bouton2_date_dernier_appui, bouton3_date_dernier_appui, bouton4_date_dernier_appui
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


# Fonction qui associe l'appui sur le bouton1 a l'appel de la fonction ci dessus
bouton1.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton2.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton3.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
bouton4.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)

#Eteindre toutes les leds
led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)


# Boucle principale
while True:
    # on attends 1ms
    time.sleep(1)
    # on regarde l'etat du bouton1
    if bouton1_actif:
        print("bouton1 actif")
        led1.toggle()
        bouton1_actif = False
    if bouton2_actif:
        print("bouton2 actif")
        led2.toggle()
        bouton2_actif = False
    if bouton3_actif:
        print("bouton3 actif")
        led3.toggle()
        bouton3_actif = False
    if bouton4_actif:
        print("bouton4 actif")
        led4.toggle()
        bouton4_actif = False
