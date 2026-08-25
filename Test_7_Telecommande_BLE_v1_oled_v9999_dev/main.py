from machine import Pin
from classe_BLEDataChat import BLEDataChat
import time
from constantes import *
       
ble_chat = BLEDataChat(MY_NAME)

led_pico = Pin('LED', Pin.OUT)
led_board = Pin(15, Pin.OUT)
bouton = Pin(14, Pin.IN, Pin.PULL_UP)

led_board.value(0)

date_dernier_appui = time.ticks_ms()
bouton_actif = False

# Fonction sera appellée lors de l'appui sur le bouton
def bouton_handler(pin):
    global bouton_actif
    global date_dernier_appui
    # on evite les rebonds ...
    if time.ticks_diff(time.ticks_ms(), date_dernier_appui) > 500: 
        bouton_actif = True
        # on reinitialise la variable date_dernier_appui
        date_dernier_appui = time.ticks_ms()

# Fonction qui associe l'appui sur le bouton a l'appel de la fonction ci dessus
bouton.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)

while True:
    if MY_NAME == "Rx":
        if (ble_chat.is_new_data_received() == 1):
            ble_chat.clear_new_data_received()
            led_board.toggle()
            print("Hello")
    else:       
        if bouton_actif:
            bouton_actif = False
            print("Bouton actif")
            ble_chat.send_data(0x11)
        else:
            print("Bouton inactif")
            ble_chat.send_default_data()
        
    time.sleep(1)
