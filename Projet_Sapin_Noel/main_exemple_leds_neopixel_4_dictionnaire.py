#=====================================================
# Main Exemple Ruban LEDs Neopixel:
# - On allume et eteint les leds en utilisant un dictionnaire
#=====================================================
from neopixel import Neopixel
import time

# DECLARATIONS:
# -------------

# declaration du ruban de leds (Pin 0)
NUMLED = 30
leds = Neopixel(NUMLED, 0, 0, "GRB")

# on place les couleurs dans un dictionnaire
colors = {"noir":(0,0,0),"blanc":(255,255,255),"vert":(0,255,0),"rouge":(255,0,0),"bleu":(0,0,255),
          "orange":(255,102,0), "jaune":(255,255,0), "violet":(128,0,128)}

# declaration du chenillard (num led, couleur)
chenillard = [(0,colors["rouge"]),(1,colors["vert"]),(2,colors["bleu"]),(3,colors["rouge"]),(4,colors["vert"]),(5,colors["bleu"]),
              (6,colors["rouge"]),(7,colors["vert"]),(8,colors["bleu"]),(9,colors["rouge"]),(10,colors["vert"]),(11,colors["bleu"]),
              (12,colors["rouge"]),(13,colors["vert"]),(14,colors["bleu"]),(15,colors["rouge"]),(16,colors["vert"]),(17,colors["bleu"]),
              (18,colors["rouge"]),(19,colors["vert"]),(20,colors["bleu"]),(21,colors["rouge"]),(22,colors["vert"]),(23,colors["bleu"]),
              (24,colors["rouge"]),(25,colors["vert"]),(26,colors["bleu"]),(27,colors["rouge"]),(28,colors["vert"]),(29,colors["bleu"])]

chenillard_arc_en_ciel = [(0,colors["rouge"]),(1,colors["rouge"]),(2,colors["rouge"]),(3,colors["orange"]),(4,colors["orange"]),(5,colors["jaune"]),
              (6,colors["jaune"]),(7,colors["vert"]),(8,colors["vert"]),(9,colors["vert"]),(10,colors["bleu"]),(11,colors["bleu"]),
              (12,colors["violet"]),(13,colors["violet"]),(14,colors["violet"]),(15,colors["violet"]),(16,colors["violet"]),(17,colors["violet"]),
              (18,colors["bleu"]),(19,colors["bleu"]),(20,colors["vert"]),(21,colors["vert"]),(22,colors["vert"]),(23,colors["jaune"]),
              (24,colors["jaune"]),(25,colors["orange"]),(26,colors["orange"]),(27,colors["rouge"]),(28,colors["rouge"]),(29,colors["rouge"])]

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
    #for element in chenillard:   # pour tous les elements de la liste chenillard
    for element in chenillard_arc_en_ciel:   # pour tous les elements de la liste chenillard
        numero_led = element[0]  # on recupere le numero de la led = premiere valeur
        couleur_led = element[1] # on recupere la couleur de cette led = seconde valeur
        # on programme la led
        leds.set_pixel(numero_led,couleur_led)
        leds.show()
        time.sleep(0.1)
    
   
    


