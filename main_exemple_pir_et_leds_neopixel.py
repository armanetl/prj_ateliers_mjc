from machine import Pin
from neopixel import Neopixel
from time import sleep

# declaration du detecteur infra rouge
pir_sensor = Pin(16, Pin.IN)

# declaration du ruban de leds (Pin 0)
NUM_LED = 30
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# on definit la luminosite des leds / 255
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

while True:
    reading = pir_sensor.value()
    #si quelquechose a ete detecte
    if reading == 1:
        print("Presence detectée")
        # on allume toutes les leds du sapin en rouge
        leds.fill((255,0,0))
        leds.show()
    #si rien  n'a ete detecte
    else:
        print("Rien a signaler")
        # on eteint les leds du sapin
        leds.clear() # equivalent a: leds.fill((0,0,0))
        leds.show()    #on attends 1 seconde    
    sleep(2)

    
   
    


