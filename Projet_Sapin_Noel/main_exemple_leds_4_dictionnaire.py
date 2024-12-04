from neopixel import Neopixel
import time

# DECLARATIONS:
# -------------

# declaration du ruban de leds (Pin 0)
NUMLED = 30
leds = Neopixel(NUMLED, 0, 0, "GRB")

# on place les couleurs dans un dictionnaire
colors = {"noir":(0,0,0),"blanc":(255,255,255),"vert":(0,255,0),"rouge":(255,0,0),"bleu":(0,0,255)}

# declaration du chenillard (num led, couleur)
chenillard = [(0,colors["rouge"]),(1,colors["vert"]),(2,colors["bleu"]),(3,colors["rouge"]),(4,colors["vert"]),(5,colors["bleu"]),
              (6,colors["rouge"]),(7,colors["vert"]),(8,colors["bleu"]),(9,colors["rouge"]),(10,colors["vert"]),(11,colors["bleu"]),
              (12,colors["rouge"]),(13,colors["vert"]),(14,colors["bleu"]),(15,colors["rouge"]),(16,colors["vert"]),(17,colors["bleu"]),
              (18,colors["rouge"]),(19,colors["vert"]),(20,colors["bleu"]),(21,colors["rouge"]),(22,colors["vert"]),(23,colors["bleu"]),
              (24,colors["rouge"]),(25,colors["vert"]),(26,colors["bleu"]),(27,colors["rouge"]),(28,colors["vert"]),(29,colors["bleu"])]


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
    
   
    


