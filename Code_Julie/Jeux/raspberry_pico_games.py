# Jeux MicroPython pour Raspberry Pi Pico
# Parfait pour enfant de 9 ans avec LEDs, boutons, capteur PIR

from machine import Pin
import time
import urandom

# Configuration commune
leds = [Pin(i, Pin.OUT) for i in (2, 3, 4, 5)]  # Utilise GPIO 2 à 5 pour LEDs
button1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
pir = Pin(15, Pin.IN)

# 1. Jeu de reaction eclair
def reaction_eclair():
    print("\nJeu : Reaction eclair")
    time.sleep(urandom.getrandbits(3))  # attente aleatoire
    leds[0].on()
    start = time.ticks_ms()
    while not button1.value():
        pass
    reaction = time.ticks_diff(time.ticks_ms(), start)
    leds[0].off()
    print(f"Temps de reaction : {reaction} ms")

# 2. Gardien du musee

def gardien_musee():
    print("\nJeu : Gardien du musee")
    print("Systeme arme... Bougez pour declencher la LED")
    while True:
        if pir.value():
            leds[1].on()
            time.sleep(1)
            leds[1].off()
            time.sleep(1)

# 3. Simon dit (version simple)
def simon_dit():
    print("\nJeu : Simon dit")
    sequence = [urandom.getrandbits(2) for _ in range(3)]
    for index in sequence:
        leds[index].on()
        time.sleep(0.5)
        leds[index].off()
        time.sleep(0.2)

    print("Repete la sequence :")
    for index in sequence:
        while True:
            if button1.value():
                pressed = 0
                break
            elif button2.value():
                pressed = 1
                break
        if pressed != (index % 2):
            print("Faux!")
            return
    print("Bravo!")

# 4. Feu de circulation
def feu_circulation():
    print("\nJeu : Feu de circulation")
    while True:
        if button1.value():
            leds[0].on()  # Rouge
            time.sleep(2)
            leds[1].on()  # Orange
            time.sleep(1)
            leds[0].off()
            leds[1].off()
            leds[2].on()  # Vert
            time.sleep(3)
            leds[2].off()

# 5. Compte a rebours mission

def mission_compte_rebours():
    print("\nJeu : Mission silencieuse")
    if button1.value():
        print("Debut du compte a rebours...")
        for i in range(10):
            time.sleep(1)
            if pir.value():
                print("Mouvement detecte! Echec.")
                leds[0].on()
                time.sleep(1)
                leds[0].off()
                return
        print("Mission reussie!")
        leds[2].on()
        time.sleep(2)
        leds[2].off()

# 6. Reflexe LED tournante
def reflexe_led_tournante():
    print("\nJeu : Reflexe LED")
    target = 2
    pos = 0
    while True:
        for i in range(len(leds)):
            leds[i].off()
        leds[pos].on()
        time.sleep(0.2)
        if button1.value():
            if pos == target:
                print("Bravo!")
                for _ in range(3):
                    leds[target].on()
                    time.sleep(0.2)
                    leds[target].off()
                    time.sleep(0.2)
                return
            else:
                print("Rate!")
                return
        pos = (pos + 1) % len(leds)

# Choisissez un jeu a tester ci-dessous, par exemple :
# reaction_eclair()
# gardien_musee()
# simon_dit()
# feu_circulation()
# mission_compte_rebours()
# reflexe_led_tournante()
