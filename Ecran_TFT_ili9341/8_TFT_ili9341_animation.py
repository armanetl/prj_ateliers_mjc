from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI

# Constants
SPI_SPEED = 10000000
#DC_PIN = Pin(6)
#CS_PIN = Pin(17)
#RST_PIN = Pin(7)
BACK_COLOR = color565(0, 0, 0)
RECT_COLOR = color565(255, 0, 0)
POLY_COLOR = color565(0, 64, 255)
CIRC_COLOR = color565(0, 255, 0)
ELLP_COLOR = color565(255, 0, 0)

# Create display object
#spi = SPI(1, baudrate=SPI_SPEED, sck=Pin(14), mosi=Pin(15))
#display = Display(spi, dc=DC_PIN, cs=CS_PIN, rst=RST_PIN)
spi = SPI(0, baudrate=10000000, sck=Pin(2), mosi=Pin(3))
display = Display(spi, dc=Pin(6), cs=Pin(5), rst=Pin(7), width=480, height=320, rotation=270)

# Draw rectangles
def draw_rectangles():
    for x in range(0, 225, 15):
        display.fill_rectangle(x, 0, 15, 227, RECT_COLOR)

# Draw polygons
def draw_polygons():
    display.fill_polygon(7, 120, 120, 100, POLY_COLOR)
    sleep(1)
    display.draw_polygon(3, 120, 286, 30, POLY_COLOR, rotate=15)
    sleep(3)

# Draw circles
def draw_circles():
    display.fill_circle(132, 132, 70, CIRC_COLOR)
    sleep(1)
    display.draw_circle(132, 96, 70, color565(0, 0, 255))
    sleep(1)

# Draw ellipses
def draw_ellipses():
    display.fill_ellipse(96, 96, 30, 16, ELLP_COLOR)
    sleep(1)
    display.draw_ellipse(96, 256, 16, 30, color565(255, 255, 0))

# Clear screen and draw shapes
display.clear(BACK_COLOR)
draw_rectangles()
display.clear(BACK_COLOR)
draw_polygons()
display.clear(BACK_COLOR)
draw_circles()
display.clear(BACK_COLOR)
draw_ellipses()

# Clean up
display.cleanup()