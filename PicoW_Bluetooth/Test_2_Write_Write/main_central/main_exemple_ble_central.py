from machine import Pin
from classe_ecranTFT import EcranTFT
import bluetooth
from ble_simple_central import BLESimpleCentral
import time 
#import framebuf, sys

def main_exemple_ble_central():
    
    print('PROG: main_exemple_ble_central')    

    TFT = EcranTFT()
    
    ble = bluetooth.BLE()
    central = BLESimpleCentral(ble)

    not_found = False

    def on_scan(addr_type, addr, name):
        if addr_type is not None:
            print("Found peripheral:", addr_type, addr, name)
            central.connect()
        else:
            nonlocal not_found
            not_found = True
            print("No peripheral found.")

    central.scan(callback=on_scan)

    # Wait for connection...
    while not central.is_connected():
        time.sleep_ms(100)
        if not_found:
            return

    print("Connected")
    TFT.tftprint("Connected.")

    def on_rx(v):
        print("RX", v)

    central.on_notify(on_rx)

    with_response = False

    i = 0
    while central.is_connected():
        try:
            v = str(i) + "_"
            print("TX", v)
            TFT.tftprint(f"TX {v}")
            central.write(v, with_response)
        except:
            print("TX failed")
            TFT.tftprint("TX failed")
        i += 1
        time.sleep_ms(400 if with_response else 30)

    print("Disconnected")
    TFT.tftprint("Disconnected.")
    
if __name__ == '__main__':    
    main_exemple_ble_central()