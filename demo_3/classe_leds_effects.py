from machine import Pin
from time import sleep


class LedsEffects:
    def __init__(self, pin_base, num_leds):
        self.led_pins = [Pin(i, Pin.OUT) for i in range(pin_base, pin_base+num_leds)]
        
    def eteindre_tout(self):
        for led in self.led_pins:
            led.off()

    # --- Animations ---
    def chenillard_aller_retour(self, delai=0.1, tours=3):
        """Effet chenillard gauche-droite puis droite-gauche"""
        for _ in range(tours):
            for i in range(4):
                self.eteindre_tout()
                self.led_pins[i].on()
                sleep(delai)
            for i in range(2, 0, -1):
                self.eteindre_tout()
                self.led_pins[i].on()
                sleep(delai)

    def clignotement_global(self, delai=0.3, tours=5):
        """Toutes les LEDs clignotent ensemble"""
        for _ in range(tours):
            for led in self.led_pins:
                led.on()
            sleep(delai)
            for led in self.led_pins:
                led.off()
            sleep(delai)

    def effet_ping_pong(self, delai=0.08, tours=3):
        """Une LED "rebondit" sur les bords"""
        position = 0
        direction = 1
        for _ in range(tours * 8):
            self.eteindre_tout()
            self.led_pins[position].on()
            sleep(delai)
            position += direction
            if position == 3 or position == 0:
                direction = -direction

    def effet_remplissage(self, delai=0.15, tours=2):
        """Les LEDs se remplissent puis se vident"""
        for _ in range(tours):
            for i in range(4):
                self.led_pins[i].on()
                sleep(delai)
            for i in range(3, -1, -1):
                self.led_pins[i].off()
                sleep(delai)


    
if __name__ == '__main__':
    leds = LedsEffects(6, 4)
    print("Eteindre tout")
    leds.eteindre_tout()
    print("Chenillard aller retour")
    leds.chenillard_aller_retour()
    print("clignotement global")
    leds.clignotement_global()
    print("Effet ping pong")
    leds.effet_ping_pong()
    print("Effet remplissage")
    leds.effet_remplissage()
