# Imports
from neopixel import Neopixel
import time

# Configuration
GPIO_NB = 12
NOMBRE_DE_LEDS = 16
COULEUR_VIOLET = (128,0,120)

# Declaration
leds = Neopixel(NOMBRE_DE_LEDS,0,GPIO_NB,"GRB")

# Variables
index = 0

# Message d'information
print("Example LEDs Neopixels....")

# Definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
#leds.clear()
# on affiche
leds.show()

# Boucle principale
while (index != 16):
    # on attends 0.5ms
    time.sleep(0.5)
    # on eteint toute les leds
    #leds.clear()
    # on allume les leds a tour de role
    leds.set_pixel(index,COULEUR_VIOLET)
    # on affiche
    leds.show()
    # on passe a la led suivante
    index = index + 1;