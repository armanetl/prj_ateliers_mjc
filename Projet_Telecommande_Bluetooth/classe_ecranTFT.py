from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI

class EcranTFT:
    def __init__(self):
        self.y_index = 0
        self.spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
        self.display = Display(self.spi, dc=Pin(6), cs=Pin(5), rst=Pin(7), width=480, height=480, rotation=270)
        
    def tftprint(self,text):
        self.y_index += 10
        if (self.y_index == 300):
            self.display.clear()
            self.y_index = 10
        self.display.draw_text8x8(10, self.y_index, text, color565(255, 255, 0),  background=0,rotate=0)
        print (self.y_index)

        
#================================
# TEST
#================================
if __name__ == '__main__':    
    print('test classe EcranTFT:')
    ecran = EcranTFT()
    for y1 in range(0,40):
        text = f"Hello {y1}"
        ecran.tftprint(text)
        sleep(0.1)

    
    
