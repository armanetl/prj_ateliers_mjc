from time import sleep
from ili9341 import Display, color565
#New lib ili9341 qui gere les image de taille full screen
from machine import Pin, SPI


def test():
    """Test code."""
    spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
    display = Display(spi, dc=Pin(6), cs=Pin(5), rst=Pin(7), width=480, height=320, rotation=270)

    display.write_cmd(display.INVON)
    #L'ecran est inverse par rapport a la lib

    # Set display color to black
    display.clear(color565(0, 0, 0))
    sleep(1)

    display.clear(color565(0, 0, 0))
    display.draw_image('./fruit2_480x320.raw', 0, 0, 480, 320)
    sleep(5)
    
    '''
    display.clear(color565(0, 0, 0))
    display.draw_image('./Furafic_Farc_resize.raw', 80, 0, 320, 320)
    sleep(1)

    display.clear(color565(0, 0, 0))
    display.draw_image('./Micropython-logo_resize.raw', 80, 0, 314, 320)
    sleep(1)

    display.clear(color565(0, 0, 0))
    display.draw_image('./Raspberry_Pi_logo_resize.raw', 80, 0, 253, 320)
    sleep(1)

    display.clear(color565(0, 0, 0))
    display.draw_image('./avatar.raw', 100, 50, 120, 120)
    sleep(1)
    '''
    display.cleanup()


test()