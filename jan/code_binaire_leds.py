from machine import Pin
from time import sleep

# Configuration des 4 LED sur les broches GPIO 2 à 5
led_pins = [Pin(i, Pin.OUT) for i in range(2, 6)]

def afficher_valeur(valeur):
    """Affiche une valeur (0–15) en binaire sur les 4 LED"""
    for i in range(4):
        bit = (valeur >> i) & 1
        led_pins[i].value(bit)

while True:
    for n in range(16):  # b0000 a b1111
        afficher_valeur(n)
        print("Affichage:", hex(n))
        sleep(0.5)  # délai entre les changements
