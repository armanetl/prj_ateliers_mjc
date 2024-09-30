# Imports
from machine import Pin
import time

# Configuration
GPIO_NB = 0

# Declaration
pir_sensor = Pin(GPIO_NB, Pin.IN)

# Boucle principale
while True:
    reading = pir_sensor.value()
    print(reading)
  