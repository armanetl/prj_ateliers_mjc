import time
# https://github.com/blaz-r/pi_pico_neopixel/wiki/Library-methods-documentation
from neopixel import Neopixel
#import myPlatformDefinitions as DEF
 
 
# valeur globale utile
colors = {"black":(0,0,0),"white":(255,255,255),"red":(0,255,0),"green":(255,0,0),"blue":(0,0,255)}

    
#-------------------------------------------------
# fonction dédiée au controle des led

pixels = None
pixels_refresh_time = None
#gpio_nb = DEF.NEOPIXEL_RING_GPIO_NB
gpio_nb = 16

def pixels_init( i_nb_leds:int, i_brightness:int ):
    global pixels
    global pixels_refresh_time
    pixels_refresh_time = time.ticks_ms()
    #attention modif ci dessous a changer en GRB
    pixels = Neopixel(i_nb_leds, 0, gpio_nb, "RGB")
    pixels.brightness(i_brightness)
    pixels.fill((0,0,0))
    print("pixels_init finished")
    
def pixels_process():
    global pixels
    global pixels_refresh_time
    if (time.ticks_ms()-pixels_refresh_time) > 20:
        # print("pixels refresh")
        pixels_refresh_time += 20
        pixels.show()

def pixels_set( i_led, i_value ):
    global pixels
    pixels.set_pixel(i_led, i_value)

#-------------------------------------------------
# fonction dédiée aux chenillards

ch_counter = 0
ch_refresh_time = None
chenillards = ((((0,"green"),(3,"black")),((0,"black"),(1,"green")),((1,"black"),(2,"green")),((2,"black"),(3,"green"))),
               (((4,"blue"),(5,"black")),((4,"black"),(5,"blue")),((5,"black"),(6,"blue")),((6,"black"),(7,"blue")),((7,"black"),(6,"blue")),((6,"black"),(5,"blue"))),
               (((11,"green"),(8,"black")),((11,"black"),(10,"green")),((10,"black"),(9,"green")),((9,"black"),(8,"green"))))

def ch_init():
    global ch_refresh_time
    ch_refresh_time = time.ticks_ms()
    print("ch_init finished")

def ch_process():
    #simple toggle chenillard with constant rate
    global ch_counter
    global ch_refresh_time
    global colors
    
    if (time.ticks_ms()-ch_refresh_time) > 200:
        print("ch_process")
        ch_refresh_time += 200
        for item in chenillards:
            for led in item[ch_counter%len(item)]:
                pixels_set(led[0], colors[led[1]])
        ch_counter += 1
        
  
#-------------------------------------------------
# programme principal    
if __name__ == '__main__':
    # initialisation, 16 leds + brightness a 10
    pixels_init( 16, 10 )
    ch_init()
    
    # boucle principale
    while True:
        ch_process()
        pixels_process()