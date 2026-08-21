"""ILI9341 demo (Scrolling Marquee)."""
from ili9341_2 import Display, color565
from time import sleep
from sys import implementation

DEF_SPI_ID = 0

DEF_TFT_SCK = 2
DEF_TFT_MOSI = 3
DEF_TFT_DC = 1
DEF_TFT_CS = 5
DEF_TFT_RST = 0

def test():
    """Scrolling Marquee."""
    try:
        from machine import Pin, SPI  # type: ignore
        cs_pin = Pin(16)
        dc_pin = Pin(4)
        rst_pin = Pin(17)
        
        '''
        # Baud rate of 40000000 seems about the max
        spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))

        # Create the ILI9341 display:
        display = Display(spi, dc=dc_pin, cs=cs_pin, rst=rst_pin)
        display.clear()
        '''

        spi = SPI(DEF_SPI_ID, baudrate=40000000, sck=Pin(DEF_TFT_SCK), mosi=Pin(DEF_TFT_MOSI))
        display = Display(spi, dc=Pin(DEF_TFT_DC), cs=Pin(DEF_TFT_CS), rst=Pin(DEF_TFT_RST), width=320, height=240, rotation=0)
        display.clear()
    
        # Draw non-moving circles
        display.fill_rectangle(0, 0, 239, 99, color565(27, 72, 156))
        display.fill_rectangle(0, 168, 239, 151, color565(220, 27, 72))

        # Load Marquee image
        display.draw_image('./Rototron128x26.raw', 56, 120, 128, 26)

        # Set up scrolling
        display.set_scroll(top=152, bottom=100)

        spectrum = list(range(152, 221)) + list(reversed(range(152, 220)))
        while True:
            for y in spectrum:
                display.scroll(y)
                sleep(.1)

    except KeyboardInterrupt:
        display.cleanup()


test()
