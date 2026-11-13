"""Animations pour un anneau NeoPixel de 16 LED sur le GPIO 16."""

import time
from neopixel import Neopixel


NB_LEDS = 24
PIN_NEOPIXEL = 16
STATE_MACHINE = 0
anneau = Neopixel(NB_LEDS, STATE_MACHINE, PIN_NEOPIXEL, "GRB")


def effacer():
    anneau.clear()
    anneau.show()


def roue_couleurs(position):
    """Retourne une couleur de l'arc-en-ciel, avec une luminosite moderee."""
    position = position % 256
    if position < 85:
        rouge = 255 - position * 3
        vert = position * 3
        bleu = 0
    elif position < 170:
        position -= 85
        rouge = 0
        vert = 255 - position * 3
        bleu = position * 3
    else:
        position -= 170
        rouge = position * 3
        vert = 0
        bleu = 255 - position * 3
    return (rouge // 4, vert // 4, bleu // 4)


def chenille_arc_en_ciel():
    """Fait tourner trois pixels colores autour de l'anneau."""
    for depart in range(NB_LEDS * 2):
        anneau.fill((0, 0, 0))
        for decalage in range(3):
            position = (depart - decalage) % NB_LEDS
            anneau[position] = roue_couleurs(position * 256 // NB_LEDS)
        anneau.show()
        time.sleep_ms(100)


def arc_en_ciel():
    """Fait tourner un arc-en-ciel complet sur l'anneau."""
    for decalage in range(64):
        for led in range(NB_LEDS):
            couleur = roue_couleurs(led * 256 // NB_LEDS + decalage * 4)
            anneau[led] = couleur
        anneau.show()
        time.sleep_ms(60)


def clignotement_couleurs():
    """Allume toutes les LED en rouge, vert, bleu et jaune."""
    couleurs = (
        (60, 0, 0),
        (0, 60, 0),
        (0, 0, 60),
        (60, 35, 0),
    )
    for couleur in couleurs:
        anneau.fill(couleur)
        anneau.show()
        time.sleep_ms(500)
    effacer()


def etoile_filante():
    """Fait avancer une etoile avec une petite trainee."""
    for depart in range(NB_LEDS * 2):
        anneau.fill((0, 0, 0))
        for decalage, intensite in ((0, 60), (1, 25), (2, 8)):
            position = (depart - decalage) % NB_LEDS
            anneau[position] = (intensite, intensite, 0)
        anneau.show()
        time.sleep_ms(100)


try:
    while True:
        clignotement_couleurs()
        chenille_arc_en_ciel()
        etoile_filante()
        arc_en_ciel()
        effacer()
        time.sleep_ms(300)
except KeyboardInterrupt:
    effacer()
