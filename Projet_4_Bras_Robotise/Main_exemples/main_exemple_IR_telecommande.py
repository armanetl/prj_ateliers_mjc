from machine import Pin
import time
from ir_rx_nec import NEC_16

data_received = False
IR_data = 0

#CH = HAUT = 0x46
#+ = BAS = 0x15
#PREV = GAUCHE = 0x44
#PLAY/PAUSE = DROITE = 0x43

#NEXT = MILIEU = 0x40

#0 = 0x16
#1 = 0x0C
#2 = 0x18
#3 = 0x5E
#4 = 0x08
#5 = 0x1C
#6 = 0x5A
#7 = 0x42
#8 = 0x52
#9 = 0x4A

def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        
ir = NEC_16(Pin(16, Pin.IN), callback)

while True:
    if data_received:
        print('Data 0x{:02x}'.format(IR_data))
        data_received = False