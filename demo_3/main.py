from machine import Pin
from time import sleep
from classe_lcd_manager import LCDManager
from classe_ir_remote import IRRemote
from classe_dht_manager import DHTManager
from classe_neopixel_effects import NeoPixelEffects
from classe_leds_effects import LedsEffects
from buzzer import Buzzer
from classe_music_P import Music_P
#import _thread

# === Initialisation des objets ===
lcd = LCDManager(5,4,2,16)
dht = DHTManager(22)
neo = NeoPixelEffects(0, 24)
buz = Buzzer(2)
buz.stop()
music = Music_P(buz)
pir_sensor = Pin(16, Pin.IN)
leds = LedsEffects(6, 4)
led_pins = [Pin(i, Pin.OUT) for i in range(6, 10)]

# === Definitions ===
Touche_0 = 0x19
Touche_1 = 0x45
Touche_2 = 0x46
Touche_3 = 0x47
Touche_4 = 0x44
Touche_5 = 0x40
Touche_6 = 0x43
Touche_7 = 0x07
Touche_8 = 0x15
Touche_9 = 0x09
Touche_H = 0x18
Touche_D = 0x5A
Touche_B = 0x52
Touche_G = 0x08
Touhe_OK = 0x1C

# === Menu principal ===
menu_items = [
    "Station meteo 🌡️",
    "Guirlande 🎄",
    "Musique 🎵",
    "Code Hexa",
    "Leds Show"
]
index = 0
mode = None

# === Fonction pour afficher le menu ===
def afficher_menu():
    lcd.clear()
    #lcd.move_to(0, 0)
    #lcd.putstr("> " + menu_items[index])
    lcd.message("> " + menu_items[index], 0)
    if index + 1 < len(menu_items):
        #lcd.move_to(0, 1)
        #lcd.putstr("  " + menu_items[index + 1])
        lcd.message("  " + menu_items[index + 1], 1)
        
# === Fonction code hexa ===
def afficher_valeur(valeur):
    """Affiche une valeur (0–15) en binaire sur les 4 LED"""
    for i in range(4):
        bit = (valeur >> i) & 1
        led_pins[i].value(bit)
        
# === Fonction de callback télécommande ===
def on_ir_command(code, addr, ext):
    #print("Code reçu:", hex(code))
    global index, mode

    if code == Touche_H:
        index = (index - 1) % len(menu_items)
        afficher_menu()

    elif code == Touche_B:
        index = (index + 1) % len(menu_items)
        afficher_menu()

    elif code == Touhe_OK:
        if index == 0:
            lcd.clear()
            lcd.message("Lecture DHT...", 0)
            t, h = dht.read()
            lcd.message(f"T:{t}C H:{h}%", 1)
            sleep(2)
        elif index == 1:
            lcd.clear()
            lcd.message("Guirlande Rouge", 0)
            neo.blink((255, 0, 0))
            lcd.clear()
            lcd.message("Animation chaud", 0)
            neo.animation_palette(neo.palette_chaud,0.1,5)
            lcd.clear()
            lcd.message("Animation froid", 0)
            neo.animation_palette(neo.palette_froid,0.1,5)
            lcd.clear()
            lcd.message("Animation Noel", 0)
            neo.animation_palette(neo.palette_noel,0.1,5)
            lcd.clear()
            lcd.message("Animation Plante OK", 0)
            neo.animation_palette(neo.palette_plante_ok,0.1,5)
            lcd.clear()
        elif index == 2:
            lcd.clear()
            lcd.message("Mode Veille", 0)
            reading = 0
            while (reading != 1):
                reading = pir_sensor.value()
                print(reading)
            lcd.clear()
            lcd.message("Mode Actif", 0)
            music.joue_melodie_timed(music.We_Wish_You_a_Merry_Christmas,5) # 5 secondes
            lcd.clear()
        elif index == 3:
            lcd.clear()
            lcd.message("Code HEXA", 0)
            for n in range(16):  # 0x0 à 0xF
                lcd.message("Valeur:" + hex(n), 1)
                afficher_valeur(n)               
                #print("Affichage:", hex(n))
                sleep(1)  # délai entre les changements       
        elif index == 4:
            lcd.clear()
            lcd.message("Leds Show", 0)
            leds.eteindre_tout()
            leds.chenillard_aller_retour()
            leds.clignotement_global()
            leds.effet_ping_pong()
            leds.effet_remplissage()
            
        afficher_menu()

    elif code == Touche_G:
        lcd.clear()
        lcd.message("Retour menu...", 0)
        sleep(1)
        afficher_menu()
        
# === Démarrage télécommande ===
remote = IRRemote(3, on_ir_command)

# === 2nd Thread ===
#def task():
#    global music
#    music.joue_melodie(music.We_Wish_You_a_Merry_Christmas)
        
#_thread.start_new_thread(task())

# === Démarrage ===
lcd.clear()
lcd.message(" Menu de Noel ", 0)
lcd.message(" MJC Raspi 2025", 1)
sleep(2)
afficher_menu()

# === Boucle principale ===
while True:
    sleep(1)