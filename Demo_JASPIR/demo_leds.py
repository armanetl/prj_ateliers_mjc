"""Petite demo lumineuse pour 4 LED branchees sur les GPIO 0 a 3."""

import time
from machine import Pin


leds = [Pin(numero, Pin.OUT) for numero in range(4)]


def afficher(nombre):
    """Affiche un nombre de 0 a 15 en binaire sur les quatre LED."""
    for position, led in enumerate(leds):
        led.value((nombre >> position) & 1)


def eteindre():
    afficher(0)


def chenille():
    """Une lumiere court d'un bout a l'autre, puis revient."""
    for position in (0, 1, 2, 3, 2, 1):
        afficher(1 << position)
        time.sleep_ms(140)


def vague():
    """Les LED s'allument les unes apres les autres, puis s'eteignent."""
    for nombre in range(1, 5):
        afficher((1 << nombre) - 1)
        time.sleep_ms(180)
    for nombre in range(3, -1, -1):
        afficher((1 << nombre) - 1)
        time.sleep_ms(180)


def compte_binaire():
    """Compte de 0 a 15 : chaque LED represente un bit."""
    for nombre in range(16):
        afficher(nombre)
        time.sleep_ms(250)


def feu_artifice():
    """Fait jaillir la lumiere depuis le centre."""
    for motif in (0b0010, 0b0110, 0b1111, 0b0110, 0b0010, 0):
        afficher(motif)
        time.sleep_ms(180)


try:
    while True:
        chenille()
        vague()
        compte_binaire()
        feu_artifice()
        time.sleep_ms(400)
except KeyboardInterrupt:
    eteindre()
