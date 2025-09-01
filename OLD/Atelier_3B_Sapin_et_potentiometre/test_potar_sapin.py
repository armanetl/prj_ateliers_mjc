from machine import Pin, ADC
from neopixel import Neopixel
import time

# configuration
NUMLED = 30

# declaration des Pin
potar = ADC(0)
#declaration (30 leds, 0, GPIO 16, 
leds = Neopixel(NUMLED,0,0,"GRB")

# fonction
def lit_potar():
    global potar
    return potar.read_u16()

def get_led_for( potar_value ):
    return (((NUMLED-1)*potar_value)/65535)


# programe principale
# initialisation des variables
old_val_potar = lit_potar()

# definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
#leds.clear()
# on affiche
leds.show()

# boucle principale
while True:
    # lit la valeur du potentiometre
    valeur_potar  = lit_potar()
    # test si la valeur lue est différente de la précédente
    if valeur_potar != old_val_potar:
        # affiche la valeur du potentiometre
        print(valeur_potar)
        # sauvegarde la nouvelle valeur du potentiometre
        old_val_potar = valeur_potar
        # converti la valeur du potentiometre en numero de led
        numero_led = int(get_led_for( valeur_potar ))
        # affiche le numero de led
        print(f"led a allume : {numero_led}")
        #leds.clear()
        leds.set_pixel(numero_led,(128,0,120))
        leds.show()
        
    time.sleep(0.3)
    
