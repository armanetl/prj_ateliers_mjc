"""ILI9341 demo (images)."""
from time import sleep
from ili9341_2 import Display, color565
from machine import Pin, SPI  # type: ignore

DEF_SPI_ID = 0

DEF_TFT_SCK = 2
DEF_TFT_MOSI = 3
DEF_TFT_DC = 1
DEF_TFT_CS = 5
DEF_TFT_RST = 0

def test():
    """Test code."""
    # Baud rate of 40000000 seems about the max
    #spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))
    #display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17))
    spi = SPI(DEF_SPI_ID, baudrate=40000000, sck=Pin(DEF_TFT_SCK), mosi=Pin(DEF_TFT_MOSI))
    display = Display(spi, dc=Pin(DEF_TFT_DC), cs=Pin(DEF_TFT_CS), rst=Pin(DEF_TFT_RST), width=320, height=240, rotation=0)
    display.clear()

    #display.write_cmd(display.INVON)
    #L'ecran est inverse par rapport a la lib

    # Set display color to black
    display.clear(color565(0, 0, 0))
    sleep(1)

    display.clear(color565(0, 0, 0))
    display.draw_image('./avatar.raw', 0, 0, 120, 120)
    sleep(1)
       
    display.draw_image('./RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    sleep(4)
    display.draw_image('./MicroPython128x128.raw', 0, 0, 128, 128)
    sleep(4)
    display.draw_image('./Tabby128x128.raw', 0, 0, 128, 128)
    sleep(4)
    display.draw_image('./Tortie128x128.raw', 0, 0, 128, 128)
    sleep(9)

    display.cleanup()


test()
