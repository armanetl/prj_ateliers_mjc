# Imports
from machine import Pin
import time

# Configuration
GPIO_NB = 0

# Declaration
LED = Pin(GPIO_NB, Pin.OUT)

# Message d'information
print("Example LED GPIO....")

# Boucle principale
while True:    
    # on eteint la led
    LED.value(0)
    # on attends 0.5 ms
    time.sleep(0.5)
    # on allume la led
    LED.value(1)
    # on attends 0.5 ms
    time.sleep(0.5)
    # on change l'etat de la led (1 vers 0)
    LED.toggle()
    # on re change l'etat de la led (0 vers 1)
    LED.toggle()