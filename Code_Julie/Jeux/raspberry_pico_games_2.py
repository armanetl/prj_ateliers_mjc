# Jeux MicroPython avancés pour Raspberry Pi Pico
# Avec 7 LEDs, 7 boutons, un buzzer, et un détecteur PIR

from machine import Pin, PWM
import time
import urandom

# --- CONFIGURATION ---
leds = [Pin(i, Pin.OUT) for i in range(2, 9)]      # GPIO 2 à 8 pour LEDs
buttons = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(9, 16)]  # GPIO 9 à 15 pour boutons
pir = Pin(16, Pin.IN)                              # GPIO 16 pour détecteur PIR
buzzer = PWM(Pin(17))                              # GPIO 17 pour buzzer

# --- UTILS ---
def play_tone(freq, duration):
    buzzer.freq(freq)
    buzzer.duty_u16(30000)
    time.sleep(duration)
    buzzer.duty_u16(0)

notes = [262, 294, 330, 349, 392, 440, 494]  # Do à Si

# --- 1. LED Magique ---
def led_magique():
    print("Jeu : LED magique")
    for _ in range(10):
        target = urandom.getrandbits(3) % 7
        leds[target].on()
        while True:
            for i, btn in enumerate(buttons):
                if btn.value():
                    if i == target:
                        play_tone(600, 0.2)
                        leds[target].off()
                        time.sleep(0.5)
                        break
                    else:
                        play_tone(150, 0.2)
                        time.sleep(0.5)
                        break
            else:
                continue
            break

# --- 2. Course contre la montre ---
def course_temps():
    print("Jeu : Course contre la montre")
    start = time.time()
    score = 0
    while time.time() - start < 30:
        target = urandom.getrandbits(3) % 7
        leds[target].on()
        t0 = time.ticks_ms()
        hit = False
        while time.ticks_diff(time.ticks_ms(), t0) < 1000:
            if buttons[target].value():
                score += 1
                play_tone(700, 0.1)
                hit = True
                break
        leds[target].off()
        if not hit:
            play_tone(200, 0.1)
    print(f"Score final : {score}")

# --- 3. Mémoire musicale ---
def memoire_musicale():
    print("Jeu : Mémoire musicale")
    sequence = [urandom.getrandbits(3) % 7 for _ in range(4)]
    for i in sequence:
        leds[i].on()
        play_tone(notes[i], 0.3)
        leds[i].off()
        time.sleep(0.2)
    print("A toi de jouer")
    for i in sequence:
        pressed = -1
        while pressed == -1:
            for j, btn in enumerate(buttons):
                if btn.value():
                    pressed = j
                    play_tone(notes[j], 0.2)
                    time.sleep(0.3)
                    break
        if pressed != i:
            play_tone(100, 0.5)
            print("Erreur!")
            return
    print("Bravo!")

# --- 4. Jeu de Ninja ---
def jeu_ninja():
    print("Jeu : Ne pas se faire detecter")
    print("Desactive le capteur PIR pendant la sequence")
    for i in range(3):
        leds[i].on()
        time.sleep(0.5)
        if pir.value():
            play_tone(100, 1)
            print("Detecte! Echec")
            for l in leds:
                l.off()
            return
        leds[i].off()
    print("Mission reussie!")
    play_tone(800, 0.5)

# --- 5. Tir au but ---
def tir_au_but():
    print("Jeu : Tir au bon moment")
    pos = 0
    direction = 1
    for _ in range(20):
        for l in leds:
            l.off()
        leds[pos].on()
        time.sleep(0.2)
        if buttons[3].value():  # bouton central
            if pos == 3:
                play_tone(1000, 0.3)
                print("Parfait!")
            else:
                play_tone(200, 0.3)
                print("Rate!")
            break
        pos += direction
        if pos == 6 or pos == 0:
            direction *= -1

# --- 6. Piano LED ---
def piano_led():
    print("Joue une melodie!")
    while True:
        for i, btn in enumerate(buttons):
            if btn.value():
                leds[i].on()
                play_tone(notes[i], 0.3)
                leds[i].off()

# --- 7. Calcul-LED ---
def calcul_led():
    print("Jeu : Calcul simple")
    for _ in range(5):
        a = urandom.getrandbits(3) % 4 + 1
        b = urandom.getrandbits(3) % 4 + 1
        result = a + b
        print(f"Combien font {a} + {b} ?")
        leds[result - 1].on()
        while True:
            for i, btn in enumerate(buttons):
                if btn.value():
                    if i + 1 == result:
                        play_tone(1000, 0.3)
                        leds[result - 1].off()
                        time.sleep(0.5)
                        break
                    else:
                        play_tone(150, 0.3)
                        time.sleep(0.5)
                        break
            else:
                continue
            break

# --- 8. Anti-fantome ---
def anti_fantome():
    print("Attrape le fantome (LED + PIR)")
    for _ in range(10):
        ghost = urandom.getrandbits(3) % 7
        leds[ghost].on()
        time.sleep(0.8)
        if pir.value():
            if buttons[ghost].value():
                print("Fantome attrape!")
                play_tone(1000, 0.2)
            else:
                print("Tu l'as rate!")
                play_tone(200, 0.2)
        leds[ghost].off()
        time.sleep(0.2)

# --- MENU POUR TEST ---
# Appeler ici les fonctions une par une pour tester
# led_magique()
# course_temps()
# memoire_musicale()
# jeu_ninja()
# tir_au_but()
# piano_led()
# calcul_led()
# anti_fantome()
