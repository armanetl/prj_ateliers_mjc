from time import sleep
from ili9341 import Display
from machine import Pin, SPI


def test():
    """Test code."""
    # Baud rate of 40000000 seems about the max
    #spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(15))
    #display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
    spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
    display = Display(spi, dc=Pin(6), cs=Pin(5), rst=Pin(7), width=320, height=480, rotation=270)

    #display.draw_image('fruits.raw', 0, 0, 240, 320)
    #def draw_image(self, path, x=0, y=0, w=320, h=240):
    #display.draw_image('./fruits.raw', 0, 0, 320, 400)
    display.draw_image('./avatar.raw', 0, 0, 120, 120)
    sleep(200)

    display.cleanup()


test()