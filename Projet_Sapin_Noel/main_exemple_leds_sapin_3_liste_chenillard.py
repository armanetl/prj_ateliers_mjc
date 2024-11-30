from machine import Pin
from neopixel import Neopixel
import time

# DECLARATIONS:
# -------------

# declaration du detecteur infra rouge
pir_sensor = Pin(16, Pin.IN)
# declaration du ruban de leds (Pin 0)
NUMLED = 30
leds = Neopixel(NUMLED, 0, 0, "GRB")

# declaration des couleurs (Rouge,Vert,Bleu)
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)

# declaration du chenillard (num led, couleur)
chenillard = [(0,couleur_rouge),(1,couleur_vert),(2,couleur_bleu),(3,couleur_rouge),(4,couleur_vert),(5,couleur_bleu)]

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
    reading = pir_sensor.value()
    print(reading)
    #si quelquechose a ete detecte
    if reading == 1:
        # on allume tour a tour les leds du sapin selon le chenillard
        for element in chenillard:   # pour tous les elements de la liste chenillard
            numero_led = element[0]  # on recupere le numero de la led = premiere valeur
            couleur_led = element[1] # on recupere la couleur de cette led = seconde valeur
            # on programme la led
            leds.set_pixel(numero_led,couleur_led)
            leds.show()
            time.sleep(0.1)
        time.sleep(1)
    #si rien  n'a ete detecte
    else:
        # on eteint les leds du sapin
        leds.clear() # equivalent a: leds.fill((0,0,0))
        leds.show()
        time.sleep(2)

    
   
    




