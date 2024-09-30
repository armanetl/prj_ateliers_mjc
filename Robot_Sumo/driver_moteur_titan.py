from machine import Pin, PWM
import time


class Moteur:
    def __init__(self, io_1, io_2):
        self.io_1 = io_1
        self.io_2 = io_2

    def marche_avant(self):
        self.io_1.value(0)
        self.io_2.value(1)
        
    def marche_arriere(self):
        self.io_1.value(1)
        self.io_2.value(0)
        
    def stop(self):
        self.io_1.value(0)
        self.io_2.value(0)
    


if __name__ == '__main__':
    print('test driver moteur')
    io_1 =Pin(8 , Pin.OUT)
    io_2 =Pin(9 , Pin.OUT)
    moteur1 = Moteur(io_1, io_2)
    io_3 =Pin(10 , Pin.OUT)
    io_4 =Pin(11 , Pin.OUT)
    moteur2 = Moteur(io_3, io_4)
    moteur1.marche_avant()
    moteur2.marche_avant()
    
    
