#=====================================================
# Main Exemple Ruban LEDs Neopixel:
# - On allume et eteint les leds separement
#=====================================================
from neopixel import Neopixel
import time

# DECLARATIONS:
# -------------

# declaration du ruban de leds (Pin 0)
NUM_LED = 30
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# declaration des couleurs (Rouge,Vert,Bleu)
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)

# INITIALISATIONS:
# ----------------

# on definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

# BOUCLE PRINCIPALE:
# ------------------

while True:
    # on allume tour a tour les leds du sapin en rouge
    for i in range (0,NUM_LED):
        leds.set_pixel(i,couleur_rouge)
        leds.show()
        time.sleep(0.1)
    time.sleep(1)
    # on allume tour a tour  les leds du sapin en vert
    for i in range (0,NUM_LED):
        leds.set_pixel(i,couleur_vert)
        leds.show()
        time.sleep(0.1)
    time.sleep(1)
    # on allume tour a tour  les leds du sapin en bleu
    for i in range (0,NUM_LED):
        leds.set_pixel(i,couleur_bleu)
        leds.show()
        time.sleep(0.1)

