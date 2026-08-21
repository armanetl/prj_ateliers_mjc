"""ILI9341 demo (inversion)."""
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

    #display.clear()
    display.fill_rectangle(4, 4, display.width // 3, display.height // 4,
                           color565(255, 0, 0))
    display.fill_polygon(3, display.width // 2, display.height // 2,
                         display.height // 8, color565(0, 255, 0), rotate=15)
    display.fill_circle(display.width - (display.width // 4),
                        display.height - (display.height // 5),
                        display.height // 6, color565(0, 0, 255))
    display.draw_image('./Python41x49.raw', display.width - 49, 0, 41, 49)

    sleep(2)
    display.invert()

    sleep(5)
    display.invert(False)

    sleep(2)
    display.cleanup()


test()
