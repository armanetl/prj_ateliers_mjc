"""ILI9341 demo (orientation)."""
from time import sleep
from ili9341_2 import Display, color565
from machine import Pin, SPI  # type: ignore
from xglcd_font import XglcdFont

DEF_SPI_ID = 0

DEF_TFT_SCK = 2
DEF_TFT_MOSI = 3
DEF_TFT_DC = 1
DEF_TFT_CS = 5
DEF_TFT_RST = 0

def test():
    """Test code."""
    print('Loading Espresso Dolce font...')
    espresso_dolce = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)
    print('Font loaded.')
    # Baud rate of 40000000 seems about the max
    '''
    spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))

    display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17),
                      width=240, height=320, rotation=0)
    '''
    spi = SPI(DEF_SPI_ID, baudrate=40000000, sck=Pin(DEF_TFT_SCK), mosi=Pin(DEF_TFT_MOSI))
    display = Display(spi, dc=Pin(DEF_TFT_DC), cs=Pin(DEF_TFT_CS), rst=Pin(DEF_TFT_RST), width=240, height=320, rotation=0)
    display.clear()



    display.draw_text(0, 0, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 255, 255))
    display.draw_text(0, 319, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 255, 0), landscape=True)
    sleep(5)

    display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17),
                      width=320, height=240, rotation=90)
    display.draw_text(0, 215, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 0, 255))
    display.draw_text(295, 239, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 255, 255), landscape=True)
    sleep(5)

    display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17),
                      width=240, height=320, rotation=180)
    display.draw_text(0, 0, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 0, 255))
    display.draw_text(0, 319, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 0, 0), landscape=True)
    sleep(5)

    display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17),
                      width=320, height=240, rotation=270)
    display.draw_text(0, 215, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(225, 0, 128))
    display.draw_text(295, 239, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 255, 0), landscape=True)
    sleep(5)
    display.cleanup()


test()
