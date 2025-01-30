#=====================================================
# Main Exemple Ruban LEDs Neopixel:
# - On allume et eteint les leds separement
# - On utilise d'autres fonctions de la lib neopixel
#=====================================================
from neopixel import Neopixel
import time

# DECLARATIONS:
# -------------

# declaration du ruban de leds (Pin 0)
NUM_LED = 30
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# declaration de quelques couleurs 
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)
couleur_noir = (0,0,0)

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
def main_demo_leds_neopixel_2_set_pixel():

    # on allume tour a tour  les leds du sapin en bleu
    for i in range (0,NUM_LED):
        leds.set_pixel(i,couleur_bleu)
        leds.show()
        time.sleep(0.1)
    leds.clear()
    leds.show()

    # on allume un bloc de leds
    leds.set_pixel_line(5,20,couleur_rouge)
    leds.show()
    time.sleep(2)
    leds.clear()
    leds.show()
    
    # on fait un gradient de couleur
    leds.set_pixel_line_gradient(5,20,couleur_vert,couleur_bleu)
    leds.show()
    time.sleep(2)
    leds.clear()
    leds.show()
    
    #Rotation d'un bloc de leds dans un sens
    leds.set_pixel_line(0,3,couleur_bleu)
    for i in range (NUM_LED):
        leds.rotate_right(1)
        leds.show()
        time.sleep (0.2)
        i=i+1 
    leds.clear()
    leds.show()

    #Rotation dans l'autre sens
    leds.set_pixel_line(0,3,couleur_vert)
    for i in range (NUM_LED):
        leds.rotate_left(1)
        leds.show()
        time.sleep (0.2)
        i=i+1 
    leds.clear()
    leds.show()

if __name__ == '__main__':
    main_demo_leds_neopixel_2_set_pixel()         
