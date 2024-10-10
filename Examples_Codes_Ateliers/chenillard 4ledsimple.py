# chenillard 4 leds simple


#Initialisation
    #import des modules
from machine import Pin
import time

    #initialisation des pins GPIO-0,1,2,3, voir tableau des Pins du Pico
led_0 = Pin(0, Pin.OUT)
led_1 = Pin(1, Pin.OUT)
led_2 = Pin(2, Pin.OUT)
led_3 = Pin(3, Pin.OUT)

# Eteindre toutes les leds
led_0.value(0)
led_1.value(0)
led_2.value(0)
led_3.value(0)

# boucle infinie
while True:
    # Pour chaque led, inverser l’état de la led
    # attendre une seconde
    led_0.toggle()
    time.sleep(1)
    led_1.toggle()
    time.sleep(1)
    led_2.toggle()
    time.sleep(1)
    led_3.toggle()
    time.sleep(1) 