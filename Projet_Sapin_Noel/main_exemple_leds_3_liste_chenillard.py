from neopixel import Neopixel
import time

# DECLARATIONS:
# -------------

# declaration du ruban de leds (Pin 0)
NUMLED = 30
leds = Neopixel(NUMLED, 0, 0, "GRB")

# declaration des couleurs (Rouge,Vert,Bleu)
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)

# declaration du chenillard (num led, couleur)
chenillard = [(0,couleur_rouge),(1,couleur_vert),(2,couleur_bleu),(3,couleur_rouge),(4,couleur_vert),(5,couleur_bleu),
              (6,couleur_rouge),(7,couleur_vert),(8,couleur_bleu),(9,couleur_rouge),(10,couleur_vert),(11,couleur_bleu),
              (12,couleur_rouge),(13,couleur_vert),(14,couleur_bleu),(15,couleur_rouge),(16,couleur_vert),(17,couleur_bleu),
              (18,couleur_rouge),(19,couleur_vert),(20,couleur_bleu),(21,couleur_rouge),(22,couleur_vert),(23,couleur_bleu),
              (24,couleur_rouge),(25,couleur_vert),(26,couleur_bleu),(27,couleur_rouge),(28,couleur_vert),(29,couleur_bleu)]

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
    # on allume tour a tour les leds du sapin selon le chenillard
    for element in chenillard:   # pour tous les elements de la liste chenillard
        numero_led = element[0]  # on recupere le numero de la led = premiere valeur
        couleur_led = element[1] # on recupere la couleur de cette led = seconde valeur
        # on programme la led
        leds.set_pixel(numero_led,couleur_led)
        leds.show()
        time.sleep(0.1)


    
   
    




