from machine import Pin
import time

# Declaration
bouton = Pin(0, machine.Pin.IN, Pin.PULL_UP) 

# Configuration des 4 LED sur les broches GPIO 6 à 9
led_pins = [Pin(i, Pin.OUT) for i in range(2, 6)]

# Variables
date_dernier_appui = time.ticks_ms()
bouton_actif = False

def afficher_valeur(valeur):
    """Affiche une valeur (0–15) en binaire sur les 4 LED"""
    for i in range(4):
        bit = (valeur >> i) & 1
        led_pins[i].value(bit)

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
bouton.irq(trigger = machine.Pin.IRQ_FALLING, handler = bouton_handler)

# Boucle principale
count = 0
while True:
    # on attends 1ms
    time.sleep(1)
    # on regarde l'etat du bouton
    if bouton_actif:
        count = count + 1
        afficher_valeur(count)
        print("Bouton actif")
        bouton_actif = False
        


