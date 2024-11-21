from machine import Pin
from neopixel import Neopixel
import time

# configuration
NUMLED = 8

# valeur globale utile
colors = {"noir":(0,0,0),"blanc":(255,255,255),"vert":(0,255,0),"rouge":(255,0,0),"bleu":(0,0,255)}

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
    
   
    


