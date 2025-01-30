#=====================================================
# Main Exemple Ruban LEDs Neopixel:
# - On allume et eteint les leds separement
# - On utilise d'autres fonctions de la lib neopixel
#=====================================================
from neopixel import Neopixel
import time

# declaration du ruban de leds (Pin 0)
NUM_LED = 8
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# declaration de quelques couleurs 
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)
couleur_noir = (0,0,0)

# on definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

# Boucle principale
while True:
    # on allume tour a tour  les leds du sapin en bleu
    for i in range (0,NUM_LED):
        leds.set_pixel(i,couleur_bleu)
        leds.show()
        time.sleep(0.1)

