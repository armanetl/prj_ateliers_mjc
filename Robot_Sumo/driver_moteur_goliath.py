from machine import Pin, PWM
import time


class Moteur:
    def __init__(self, io_1, io_2, io_pwm, frequency = 5000):
        self.io_1 = io_1
        self.io_2 = io_2
        self.io_pwm = PWM(io_pwm)
        self.io_pwm.freq(frequency)


    def marche_avant(self,vitesse=100):
        self.io_1.value(1)
        self.io_2.value(0)
        self.io_pwm.duty_u16(int(65536*(vitesse/100)))
        

    def marche_arriere(self,vitesse=100):
        self.io_1.value(0)
        self.io_2.value(1)
        self.io_pwm.duty_u16(int(65536*(vitesse/100)))
        
    def stop(self):
        self.io_1.value(1)
        self.io_2.value(1)
    


if __name__ == '__main__':
    print('test driver moteur')
    io_1 =Pin(14 , Pin.OUT)
    io_2 =Pin(15 , Pin.OUT)
    io_pwm =Pin(13 )
    moteur = Moteur(io_1, io_2, io_pwm)
    moteur.marche_avant()
    
    
    
    