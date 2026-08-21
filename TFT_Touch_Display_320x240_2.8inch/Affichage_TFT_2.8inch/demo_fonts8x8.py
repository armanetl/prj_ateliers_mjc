"""ILI9341 demo (fonts 8x8)."""
from time import sleep
from ili9341_2 import Display, color565
from machine import Pin, SPI  # type: ignore


def test():
    """Test code."""
    '''
    spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))
    display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17))
    '''
    #spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
    #display = Display(spi, dc=Pin(6), cs=Pin(5), rst=Pin(7), width=480, height=320, rotation=270)
    spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
    display = Display(spi, dc=Pin(1), cs=Pin(5), rst=Pin(0), width=320, height=240, rotation=0)
    display.clear()

    x_center = display.width // 2
    y_center = display.height // 2

    display.draw_text8x8(0, 0, 'Built-in', color565(255, 0, 255))
    display.draw_text8x8(16, 16, 'MicroPython', color565(255, 255, 0))
    display.draw_text8x8(32, 32, '8x8 Font', color565(0, 0, 255))
    
    display.draw_text8x8(x_center - 40, 120, "Rotate = 0",
                         color565(0, 255, 0))
    display.draw_text8x8(0, y_center - 44, "Rotate = 90",
                         color565(255, 0, 0), rotate=90)
    display.draw_text8x8(x_center - 48, display.height - 9, "Rotate = 180",
                         color565(0, 255, 255), rotate=180)
    display.draw_text8x8(display.width - 9, y_center - 48, "Rotate = 270",
                         color565(255, 255, 255), rotate=270)

    display.draw_text8x8(x_center - 40, 140, "Rotate = 0",
                         color565(0, 255, 0), background=color565(255, 0, 0))
    display.draw_text8x8(20, y_center - 44, "Rotate = 90", color565(255, 0, 0),
                         rotate=90, background=color565(0, 255, 0))
    display.draw_text8x8(x_center - 48, display.height - 29, "Rotate = 180",
                         color565(0, 255, 255), rotate=180,
                         background=color565(0, 0, 255))
    display.draw_text8x8(display.width - 29, y_center - 48, "Rotate = 270",
                         color565(255, 255, 255), rotate=270,
                         background=color565(255, 0, 255))

    sleep(15)
    display.cleanup()


test()
