#Chenillard 4 leds simple

#Import des modules
from machine import Pin
import time

#Initialisation des leds
led_0 = Pin(0, Pin.OUT)
led_1 = Pin(1, Pin.OUT)
led_2 = Pin(2, Pin.OUT)
led_3 = Pin(3, Pin.OUT)
led_10 = Pin(6, Pin.OUT)
led_11 = Pin(7, Pin.OUT)
led_12 = Pin(8, Pin.OUT)
led_13 = Pin(9, Pin.OUT)

#Eteindre toutes les leds
led_0.value(0)
led_1.value(0)
led_2.value(0)
led_3.value(0)
led_10.value(0)
led_11.value(0)
led_12.value(0)
led_13.value(0)

#Boucle infinie
while True:
    # Pour chaque led, inverser l’état de la led
    # Attendre une seconde
    led_0.toggle()
    time.sleep(1)
    led_1.toggle()
    time.sleep(1)
    led_2.toggle()
    time.sleep(1)
    led_3.toggle()
    time.sleep(1)
    led_10.toggle()
    time.sleep(1)
    led_11.toggle()
    time.sleep(1)
    led_12.toggle()
    time.sleep(1)
    led_13.toggle()
    time.sleep(1) 