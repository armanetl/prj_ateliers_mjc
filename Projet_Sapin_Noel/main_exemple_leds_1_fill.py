from neopixel import Neopixel
import time

# DECLARATIONS:
# -------------

# declaration du ruban de leds (Pin 0)
NUMLED =30
leds = Neopixel(NUMLED, 0, 0, "GRB")

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
    # on allume toutes les leds du sapin en rouge
    leds.fill((255,0,0))
    leds.show()
    time.sleep(1)
    # on allume toutes les leds du sapin en vert
    leds.fill((0,255,0))
    leds.show()
    time.sleep(1)
    # on allume toutes les leds du sapin en bleu
    leds.fill((0,0,255))
    leds.show()
    time.sleep(1)    

