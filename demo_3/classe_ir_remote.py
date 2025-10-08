from machine import Pin
from ir_rx_nec import NEC_16

class IRRemote:
    def __init__(self, pin_num, callback):
        self.ir = NEC_16(Pin(pin_num, Pin.IN), callback)

