from machine import Pin
from classe_ecranTFT import EcranTFT
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
import time 

def main_exemple_ble_peripheral():
    
    print('PROG: main_exemple_ble_peripheral')
    
    TFT = EcranTFT()
    
    ble = bluetooth.BLE()        
    p = BLESimplePeripheral(ble)

    def on_rx(v):
        print("RX", v)

    p.on_write(on_rx)

    i = 0
    while True:
        TFT.tftprint("Wait connection....")
        if p.is_connected():
            TFT.tftprint("Peripheral is connected")
            # Short burst of queued notifications.
            for _ in range(3):
                data = str(i) + "_"
                print("TX", data)
                p.send(data)
                TFT.tftprint(f"Send data {data}")
                i += 1
        time.sleep_ms(100)

if __name__ == '__main__':    
    main_exemple_ble_peripheral()