Ecran OLED SSD1306 (#4euros) ** I2C **
======================================
Pas de couleur, juste une bande jaune
128x64  0.96" : Achats divers (Augmenter la frequence pour 64 sinon timeout)
128x32  0.91" : Robot Jaune

Ecran OLED 128x128  1.5" (#15euros) 
======================================
Pas acheté, pas tres compétitif


Ecran OLED ST7789 (#11euros) ** SPI **
======================================
Couleurs !!!
240x135  1.14" : Robot Blanc


Ecran OLED ILI9341 (#15euros) ** SPI **
======================================
Couleurs !!!

320x240  2.8" : Achat Amazon pour jeux d'arcade
-----------------------------------------------

    spi1 = SPI(DEF_SPI_ID, baudrate=40000000, sck=Pin(DEF_TFT_SCK), mosi=Pin(DEF_TFT_MOSI))
    display = Display(spi1, dc=Pin(DEF_TFT_DC), cs=Pin(DEF_TFT_CS), rst=Pin(DEF_TFT_RST), width=320, height=240, rotation=0)
    display.clear()

    spi2 = SPI(1, baudrate=1000000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
    Demo(display, spi2)

        self.touch = Touch(spi2,cs=Pin(13),int_pin=Pin(6),int_handler=self.touchscreen_press,width=320,height=240)



     
    Branchements:
    ----------------- TFT - Display (SPI0)
    VCC: 3.3v
    GND
    PIN_TFT_CS = 5
    PIN_TFT_RST = 0
    PIN_TFT_DC = 1
    PIN_TFT_TX = 3 #MOSI
    PIN_TFT_SCK = 2
    LED: 5v
    PIN_TFT_RX = 4 #MISO 
    ------------------ Touch (SPI1)
    T_CLK = 10
    T_CS = 13  
    T_DIN (MOSI) = 11
    T_DO (MISO) = 12
    T_IRQ (TPINT interrupt) = 6
    ------------------

    Ne peut utiliser un GT911, il faut pour cet ecran un XPT2046.


320x480  3.5" : Pico Breadboard Kit
-----------------------------------------------

    spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
    display = Display(spi, dc=Pin(6), cs=Pin(5), rst=Pin(7), width=480, height=320, rotation=270)

    Touch:         
    self.i2c = machine.I2C(0,freq=freq, scl=machine.Pin(scl), sda=machine.Pin(sda)) # PG : ajout id=0
    spiTFT = SPI(0, baudrate=40000000, sck=Pin(self.TFT_CLK_PIN), mosi=Pin(self.TFT_MOSI_PIN))

    #TFT: SPI Id 0 (lib ili9341)
    TFT_RST_PIN = const(7)
    TFT_DC_PIN = const(6)
    TFT_CLK_PIN = const(2)
    TFT_MOSI_PIN = const(3)
    TFT_MISO_PIN = const(4)
    TFT_CS_PIN = const(5)

    #Touch: I2C Id 0 (lib GT911)
    TOUCH_I2C_SDA_PIN = const(8)
    TOUCH_I2C_SCL_PIN = const(9)
    TOUCH_RESET_PIN = const(10) # TPRST reset
    TOUCH_INT_PIN = const(11) # TPINT interrupt





