from machine import Pin
from neopixel import Neopixel
import time

# configuration
NUMLED = 30

# valeur globale utile
colors = {"noir":(0,0,0),"blanc":(255,255,255),"vert":(0,255,0),"rouge":(255,0,0),"bleu":(0,0,255)}

# declaration du detecteur infra rouge
pir_sensor = Pin(16, Pin.IN)
# declaration du ruban de leds (Pin 0)
leds = Neopixel(NUMLED, 0, 0, "GRB")

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
        # on allume tour a tour les leds du sapin en rouge
        for i in range (0,NUMLED):
            leds.set_pixel(i,colors["rouge"])
            leds.show()
            time.sleep(0.2)
        time.sleep(1)
        # on allume tour a tour les leds du sapin en bleu
        for i in range (0,NUMLED):
            leds.set_pixel(i,colors["bleu"])
            leds.show()
            time.sleep(0.2)
        time.sleep(1)
        # on allume tour a tour les leds du sapin en vert
        for i in range (0,NUMLED):
            leds.set_pixel(i,colors["vert"])
            leds.show()
            time.sleep(0.2)
        time.sleep(1)
    #si rien  n'a ete detecte
    else:
        # on eteint les leds du sapin
        leds.fill((0,0,0))
        leds.show()        
    time.sleep(1)
    
   
    


