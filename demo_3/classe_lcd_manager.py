from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd

class LCDManager:
    def __init__(self, scl_pin=5, sda_pin=4, rows=2, cols=16):
        self.i2c = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
        self.addr = self.i2c.scan()[0]
        self.lcd = I2cLcd(self.i2c, self.addr, rows, cols)
    
    def clear(self):
        self.lcd.clear()
    
    def message(self, text, line=0):
        """Affiche du texte sur une ligne"""
        self.lcd.move_to(0, line)
        self.lcd.putstr(text)

if __name__ == '__main__':
    lcd = LCDManager()
    lcd.message("Test LCDManager", 0)
