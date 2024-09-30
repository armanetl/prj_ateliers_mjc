# Imports
from machine import Pin
import time

# Configuration
GPIO_NB = 19

# Declaration
bouton = Pin(GPIO_NB, Pin.IN, Pin.PULL_UP)

# Variables
date_dernier_appui = time.ticks_ms()
bouton_actif = False

# Fonction sera appellée lors de l'appui sur le bouton
def bouton_handler(pin):
    global bouton_actif
    global date_dernier_appui
    # on evite les rebonds ...
    if time.ticks_diff(time.ticks_ms(), date_dernier_appui) > 500: 
        bouton_actif = True
        # on reinitialise la variable date_dernier_appui
        date_dernier_appui = time.ticks_ms() 

# Fonction qui associe l'appui sur le bouton a l'appel de la fonction ci dessus
bouton.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)

# Message d'information
print("Example Boutons et Interruptions....")

# Boucle principale
while True:
    # on attends 1ms
    time.sleep(1)
    # on regarde l'etat du bouton
    if bouton_actif:
        bouton_actif = False
        print("Bouton actif")
    else:
        print("Bouton inactif")
