from machine import Pin
from neopixel import Neopixel
import time


# declaration du detecteur infra rouge
pir_sensor = Pin(16, Pin.IN)
#declaration du ruban de leds (Pin 0)
leds = Neopixel(30, 0, 0, "GRB")

# definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
#leds.clear()
# on affiche
leds.show()

#boucle principale
while True:
    reading = pir_sensor.value()
    print(reading)
    #si quelquechose a ete detecte
    if reading == 1:
        # on allume les leds du sapin en rouge
        leds.fill((255,0,0))
        leds.show()
        time.sleep(2)
        # on allume les leds du sapin en bleu
        leds.fill((0,0,255))
        leds.show()
        time.sleep(2)    
        # on allume les leds du sapin en vert
        leds.fill((0,255,0))
        leds.show()
        time.sleep(2)
    #si rien  n'a ete detecte
    else:
        # on eteint les leds du sapin
        leds.fill((0,0,0))
        leds.show()        
    time.sleep(1)
    
   
    


