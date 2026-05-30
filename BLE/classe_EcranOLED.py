from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf #Logos micropyton & raspberry
import sys      #Test addr I2C
import time

class EcranOLED:
    def __init__(self,text = ""):        
        self.i2c =I2C(0,sda=Pin(16), scl=Pin(17), freq=200000) #Augmenter la frequence pour le 128x64 sinon timeout
        self.i2c_addr = [hex(ii) for ii in self.i2c.scan()]    
        if not self.i2c_addr:
            print('No I2C Display Found')
            sys.exit()
        else:
            print("I2C Address      : {}".format(self.i2c_addr[0]))
            print("I2C Configuration: {}".format(self.i2c))
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        self.title = text
        self._lines = []
        self._max_lines = 4

    def DisplayClear(self):
        # Display text on the OLED
        self.oled.fill(0) 
        #self.oled.show()

    def DisplayText(self,text,x0,y0):
        # Display text on the OLED
        #self.DisplayClear() 
        self.oled.text(self.title, 0, 0)
        #self.oled.text("Pico", 0, 10)
        self.oled.fill_rect(0, y0, 128, 8, 0) #Efface la ligne avant de la re-ecrire
        self.oled.text(text, x0, y0)
        self.oled.show()

    def DisplayMessage(self,text):
        # Display text on the OLED
        #self.DisplayClear() 
        self.oled.text(self.title, 0, 0)
        #self.oled.text("Pico", 0, 10)
        self.oled.fill_rect(0, 20, 128, 8, 0) #Efface la ligne avant de la re-ecrire
        self.oled.text(text, 0, 20)
        self.oled.show()

    def DisplayLog(self, msg):
        self._lines.append(msg)
        if len(self._lines) > self._max_lines:
            self._lines.pop(0)
        self.oled.fill(0)
        self.oled.text(self.title, 0, 0)
        y = 20
        for line in self._lines:
            self.oled.text(line[:21], 0, y)
            y += 10
        self.oled.show()
    
    def display_logo_raspberry(self,x0,y0):
        # Display the Raspberry Pi logo on the OLED
        buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)        
        self.DisplayClear() 
        self.oled.blit(fb, x0, y0)
        self.oled.show()
        
    def display_logo_micropython(self,x0,y0):
        # Display the Micropython logo on the OLED
        buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x10\x8a\n0\x10$\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\xfe\xff?\xfe\xfd|\xfb\xf8\xfc\xff|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@\xe0\xe0\xe0\xc0\xc1c\x9f\xff\x0f\xce\xff\xff\xcf\xe3\xf0pp\xa0\xe0\xe0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xff\xfb\xe7\xdf\x8e\x9e\xfd\x95"$%\x00\xfe\xff\xff\xed\xdd\xce\xce\xff\xe7\xe7\xf7\xfb\xf9\xfep\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@6\x9bg7\xcfo\x9d\xdb?\xbbws\xf7\xfa\xfa\xf9\xf4\xfd\xf7\xf3\xf1\xfdsy\xbd;\xd9\x9do\xcc6g\x9b6@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\t\x06\x13\x0c&\x19\r\x1b\x1b\r\x19&\x0c\x13\x06\t\x03\x04\x01\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        fb = framebuf.FrameBuffer(buffer, 48, 48, framebuf.MVLSB)
        self.DisplayClear() 
        self.oled.blit(fb, x0, y0)
        self.oled.show()

    #GIMP
    #Image de départ en couleur avec definition > 128x64
    #Image -> Mode -> Couleurs indexées -> Utiliser une palette noir et blanc (1bit)
    #Image -> Echelle -> Taille de l'image -> max 128 pixels large et 64 pixels hauteur
    #Couleurs -> Inverser (pour inverser le noir et le blanc)
    # ou utiliser le pico pour inverser (oled.invert(1))
    #Fichier -> Exporter sous -> .pbm (choisir formatage de type raw)
    def display_pbm(self,image,width,height,x0,y0):        
        self.DisplayClear() 
        with open(image, 'rb' ) as f:
            f.readline() # Magic number    P4 for pbm (Portable Bitmap)
            f.readline() # Creator comment
            f.readline() # Dimensions
            data = bytearray(f.read())
        fbuf = framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)
        self.oled.invert(1)
        self.oled.blit(fbuf, x0, y0)
        self.oled.show()
    
    
#================================
# TEST
#================================
if __name__ == '__main__':    
    print('test classe EcranOLED:')
    ecran = EcranOLED("Recepteur")
    #ecran.display_logo_raspberry(0,15)
    #time.sleep(2)
    #ecran.display_logo_micropython(0,15)
    #time.sleep(2)
    #ecran.display_pbm('upy-logo_128_64.pbm',128,64)
    #time.sleep(2)
    #ecran.display_pbm('avatar2_63_64.pbm',63,64,60,0)
    #time.sleep(2)
    ecran.DisplayClear()

 
    y1 = 0
    data = 0

    while True:
        text = f"Data {data}"
        position = 20 + y1 * 10

        if position > 50:
            y1 = 0
            continue

        ecran.DisplayText(text, 0, position)

        y1 += 1
        data += 1
        time.sleep(0.1)
    
    
