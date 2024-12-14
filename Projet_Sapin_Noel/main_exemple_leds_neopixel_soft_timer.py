#=====================================================
# Main Exemple Ruban LEDs Neopixel:
# - On allume et eteint les leds en utilisant le timer interne du pico
#=====================================================
from machine import Pin, Timer
from utime import sleep
from neopixel import Neopixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 24
leds = Neopixel(NUMBER_PIXELS,NEOPIXEL_PIN, 0, "GRB")

# on definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

# create an uninitialized timer object
myTimer = Timer()

counter = 0
# a callback function.  Use this with a timer that triggers 20 times a second
def move_pixel(myTimer):
    global counter
    for i in range(0, NUMBER_PIXELS):
        if i == counter:
            leds.set_pixel(i,(10,0,0))
        else:
            leds.set_pixel(i,(0,0,10))
        leds.show()
    counter += 1
    if counter > NUMBER_PIXELS:
        counter = 0

# initialize the timer object to tick 20 times per second (50 milliseconds)
myTimer.init(period=50, mode=Timer.PERIODIC, callback=move_pixel)

while True:
    print('Just sleeping here.  The timer is doing all the work flashing the LED...', counter)
    sleep(5) # sleep for five seconds