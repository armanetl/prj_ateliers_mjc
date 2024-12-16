#=====================================================
# Main Exemple Boutons & Interruptions:
# - Un appui sur les boutons déclenche une interruption
# - Le CPU execute un handler (= routine d'interruption)
#   qui va setter une variable
# - On toggle des LEDs a chaque appui sur les boutons
#=====================================================
# Imports
from machine import Pin
import time

# Declaration des boutons
boutons = [Pin(14, Pin.IN, Pin.PULL_UP),Pin(15, Pin.IN, Pin.PULL_UP),
           Pin(17, Pin.IN, Pin.PULL_UP),Pin(18, Pin.IN, Pin.PULL_UP),
           Pin(19, Pin.IN, Pin.PULL_UP),Pin(20, Pin.IN, Pin.PULL_UP),
           Pin(21, Pin.IN, Pin.PULL_UP),Pin(22, Pin.IN, Pin.PULL_UP)]

# Declaration des leds
leds = [Pin(6, Pin.OUT),Pin(7, Pin.OUT),
        Pin(8, Pin.OUT),Pin(9, Pin.OUT),
        Pin(10, Pin.OUT),Pin(11, Pin.OUT),
        Pin(12, Pin.OUT),Pin(13, Pin.OUT)]

# Variables
boutons_date_dernier_appui = [time.ticks_ms(),time.ticks_ms(),
                              time.ticks_ms(),time.ticks_ms(),
                              time.ticks_ms(),time.ticks_ms(),
                              time.ticks_ms(),time.ticks_ms()]

boutons_actif = [False,False,False,False,False,False,False,False]

# Fonction sera appellée lors de l'appui sur le bouton1
def bouton_handler(pin):
    global boutons_actif
    global boutons_date_dernier_appui
    if (pin == boutons[0]):
        i = 0
    if (pin == boutons[1]):
        i = 1
    if (pin == boutons[2]):
        i = 2
    if (pin == boutons[3]):
        i = 3
    if (pin == boutons[4]):
        i = 4
    if (pin == boutons[5]):
        i = 5
    if (pin == boutons[6]):
        i = 6   
    if (pin == boutons[7]):
        i = 7
    # on evite les rebonds ...
    if time.ticks_diff(time.ticks_ms(), boutons_date_dernier_appui[i]) > 500: 
        boutons_actif[i] = True
        # on reinitialise la variable bouton_date_dernier_appui
        boutons_date_dernier_appui[i] = time.ticks_ms() 



# Fonction qui associe l'appui sur le bouton1 a l'appel de la fonction ci dessus
for bouton in boutons:
    bouton.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)

#Eteindre toutes les leds
for led in leds:
    led.value(0)


# Boucle principale
while True:
    # on attends
    time.sleep(0.2)
    # on regarde l'etat des boutons
    for i in range(8):
        if boutons_actif[i]:
            print("bouton " + str(i) + " actif")
            leds[i].toggle()
            boutons_actif[i] = False
