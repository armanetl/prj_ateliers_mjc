from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI


def test():
    """Test code."""
    # Baud rate of 40000000 seems about the max
    #spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(15))
    #display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
    spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
    display = Display(spi, dc=Pin(6), cs=Pin(5), rst=Pin(7), width=320, height=480)

    # Set display color to red
    display.clear(color565(255, 0, 0))
    sleep(1)

    # Set display color to orange
    display.clear(color565(255, 128, 0))
    sleep(1)

    # Set display color to yellow
    display.clear(color565(255, 255, 0))
    sleep(1)

    # Set display color to green
    display.clear(color565(0, 255, 0))
    sleep(1)

    # Set display color to blue
    display.clear(color565(0, 0, 255))
    sleep(1)

    # Set display color to purple
    display.clear(color565(128, 0, 128))
    sleep(1)

    # Set display color to pink
    display.clear(color565(255, 192, 203))
    sleep(1)

    # Set display color to brown
    display.clear(color565(139, 69, 19))
    sleep(1)

    # Set display color to gray
    display.clear(color565(128, 128, 128))
    sleep(1)

    # Set display color to white
    display.clear(color565(255, 255, 255))
    sleep(1)

test()