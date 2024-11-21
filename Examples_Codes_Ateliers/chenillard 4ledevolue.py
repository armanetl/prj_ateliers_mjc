# chenillard 4 leds evolue


#Initialisation
#import des modules
from machine import Pin
import time

#initialisation des pins GPIO-0,1,2,3, voir tableau des Pins du Pico
led_0 = Pin(2, Pin.OUT)
led_1 = Pin(3, Pin.OUT)
led_2 = Pin(4, Pin.OUT)
led_3 = Pin(5, Pin.OUT)

# déclarer une liste de leds
LED = [led_0,led_1,led_2,led_3,led_3,led_2,led_1,led_0]
#initialiser les leds
for led in LED:
    led.value(0)

# boucle infinie
while True:
    # Pour chaque led de la liste, inverser l’état de la led
    # attendre une seconde
    for led in LED:
        led.toggle()
        time.sleep(1)
    
