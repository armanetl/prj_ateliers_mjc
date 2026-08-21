"""ILI9341 demo (simple touch demo)."""
from ili9341_2 import Display, color565
from xpt2046 import Touch
from machine import idle, Pin, SPI  # type: ignore

DEF_SPI_ID = 0

DEF_TFT_SCK = 2
DEF_TFT_MOSI = 3
DEF_TFT_DC = 1
DEF_TFT_CS = 5
DEF_TFT_RST = 0


class Demo(object):
    """Touchscreen simple demo."""
    CYAN = color565(0, 255, 255)
    PURPLE = color565(255, 0, 255)
    WHITE = color565(255, 255, 255)

    def __init__(self, display, spi2):
        self.display = display
        self.touch = Touch(spi2,cs=Pin(13),int_pin=Pin(6),int_handler=self.touchscreen_press,width=320,height=240)

        # Display initial message
        self.display.draw_text8x8(self.display.width // 2 - 32,self.display.height - 9,"TOUCH ME",self.WHITE,background=self.PURPLE)

        # A small 5x5 sprite for the dot
        self.dot = bytearray(b'\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00')

    def touchscreen_press(self, x, y):
        # Conversion coordonnées tactile -> écran
        screen_x = int((y - 9) * 319 / (230 - 9))
        screen_y = int((x - 27) * 239 / (296 - 27))
        # Limitation aux dimensions de l'écran
        screen_x = max(0, min(319, screen_x))
        screen_y = max(0, min(239, screen_y))
        self.display.draw_text8x8(self.display.width // 2 - 32,self.display.height - 9,"{0:03d}, {1:03d}".format(screen_x, screen_y),self.CYAN)

        self.display.draw_sprite(self.dot,screen_x - 2,screen_y - 2,5,5)

def test():
    spi1 = SPI(DEF_SPI_ID, baudrate=40000000, sck=Pin(DEF_TFT_SCK), mosi=Pin(DEF_TFT_MOSI))
    display = Display(spi1, dc=Pin(DEF_TFT_DC), cs=Pin(DEF_TFT_CS), rst=Pin(DEF_TFT_RST), width=320, height=240, rotation=0)
    display.clear()

    spi2 = SPI(1, baudrate=1000000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
    Demo(display, spi2)

    try:
        while True:
            idle()

    except KeyboardInterrupt:
        print("\nCtrl-C pressed.  Cleaning up and exiting...")
    finally:
        display.cleanup()


test()
