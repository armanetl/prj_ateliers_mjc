from machine import Pin
from classe_ecranTFT import EcranTFT
import time 

def main_exemple_display_messages():
    print('PROG: main_exemple_display_messages')    
    TFT = EcranTFT()
    for y1 in range(0,40):
        text = f"Hello {y1}"
        TFT.tftprint(text)
        time.sleep(0.1)

if __name__ == '__main__':    
    main_exemple_display_messages()
