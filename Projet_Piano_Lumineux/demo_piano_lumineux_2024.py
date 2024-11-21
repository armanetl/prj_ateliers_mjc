from machine import Pin,PWM
import time
import utime
from time import sleep
from neopixel import Neopixel

'''
########################
Mode 1: Piano simple
Mode 2: Leds s allument sur une chanson
Mode 3: Leds s allument pour indiquer ce qu on doit jouer
Mode 4: Jeu Simon
#######################
'''
MODE = 2

button_do = Pin(6, Pin.IN, Pin.PULL_UP)
button_re = Pin(7, Pin.IN, Pin.PULL_UP)
button_mi = Pin(8, Pin.IN, Pin.PULL_UP)
button_fa = Pin(9, Pin.IN, Pin.PULL_UP)

do_last = time.ticks_ms()
re_last = time.ticks_ms()
mi_last = time.ticks_ms()
fa_last = time.ticks_ms()

# frequences des notes
freq_notes = {"do":1046,"re":1175,"mi":1318,"fa":1397,"so":1568,"la":1760,"si":1967}
led_notes = {"do":0,"re":1,"mi":2,"fa":3,"so":4,"la":5,"si":6}

# declaration du buzzer 
buz = PWM(Pin(15))

# configuration
NUMLED = 8

# valeur globale utile
colors = {"noir":(0,0,0),"blanc":(255,255,255),"vert":(0,255,0),"rouge":(255,0,0),"bleu":(0,0,255)}

# declaration du ruban de leds (Pin 0)
leds = Neopixel(NUMLED, 0, 0, "GRB")

# definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
#leds.clear()
# on affiche
leds.show()


# fonction qui va jouer une note
def joue_note(val_note,time):
    global buz
    buz.freq(freq_notes[val_note])
    buz.duty_u16(1000) #volume
    sleep(time)



def button_handler(pin):
        global do_last, re_last, mi_last, fa_last
        global button_do, button_re, button_mi, button_fa
      
        if pin is button_do:
            if time.ticks_diff(time.ticks_ms(), do_last) > 500:
                print('DO')
                leds.fill((0,0,0))
                leds.show()
                leds.set_pixel(led_notes["do"],colors["rouge"])
                leds.show()
                joue_note("do",0.25)
                do_last = time.ticks_ms()
        elif pin is button_re:
            if time.ticks_diff(time.ticks_ms(), re_last) > 500:
                print('RE')
                leds.fill((0,0,0))
                leds.show()
                leds.set_pixel(led_notes["re"],colors["rouge"])
                leds.show()
                re_last = time.ticks_ms()
                joue_note("re",0.25)
        elif pin is button_mi:
            if time.ticks_diff(time.ticks_ms(), mi_last) > 500:
                print('MI')
                leds.fill((0,0,0))
                leds.show()
                leds.set_pixel(led_notes["mi"],colors["rouge"])
                leds.show()
                joue_note("mi",0.25)
                mi_last = time.ticks_ms()
        elif pin is button_fa:
            if time.ticks_diff(time.ticks_ms(), fa_last) > 500:
                print('FA')
                leds.fill((0,0,0))
                leds.show()
                leds.set_pixel(led_notes["fa"],colors["rouge"])
                leds.show()
                joue_note("fa",0.25)
                fa_last = time.ticks_ms()
                
button_do.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_re.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_mi.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_fa.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
     
if MODE == 2:
    
    notes = ["mi","mi","mi"   ,"mi","mi","mi" ,"mi","so","do","re"   ,"mi"  ,"fa","fa","fa"   ,"mi","mi","mi"  ,"re","re","re","mi"  ,"re","so"]
    duree = [0.25,0.25,0.5    ,0.25,0.25,0.5  ,0.25,0.25,0.25,0.25   ,1     ,0.25,0.25,0.5    ,0.25,0.25,0.5   ,0.25,0.25,0.25,0.25  ,0.5,0.5]
    pause = [0.01,0.01,0.01   ,0.01,0.01,0.01 ,0,0,0,0               ,0     ,0.01,0.01,0.01   ,0.01,0.01,0.01  ,0.01,0.01,0,0.01     ,0,0]

    notes2 = ["mi","mi","mi"   ,"mi","mi","mi" ,"mi","so","do","re"   ,"mi"  ,"fa","fa","fa"   ,"mi","mi","mi"  ,"so","fa","mi","re"  ,"do"]
    duree2 = [0.25,0.25,0.5    ,0.25,0.25,0.5  ,0.25,0.25,0.25,0.25   ,1     ,0.25,0.25,0.5    ,0.25,0.25,0.5   ,0.25,0.25,0.25,0.25  ,1]
    pause2 = [0.01,0.01,0.01   ,0.01,0.01,0.01 ,0,0,0,0               ,0     ,0.01,0.01,0.01   ,0.01,0.01,0.01  ,0,0,0,0              ,0]

    while True:
        # joue la partie 1
        index = 0
        for note in notes:
            leds.fill((0,0,0))
            leds.show()
            leds.set_pixel(led_notes[note],colors["rouge"])
            leds.show()
            joue_note(note,duree[index])
            sleep(pause[index])
            index = index+1
        # joue la partie 2
        index = 0
        for note in notes2:
            leds.fill((0,0,0))
            leds.show()
            leds.set_pixel(led_notes[note],colors["rouge"])
            leds.show()
            joue_note(note,duree2[index])
            sleep(pause2[index])
            index = index+1
