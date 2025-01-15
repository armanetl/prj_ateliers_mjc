from pico_car_mjc import pico_car
import time

        
class Moteur():
    def __init__(self, pico_car, moteur_cote = 'l'):
        self.picocar = pico_car
        self.moteur_cote = moteur_cote

    def marcheAvant(self, vitesse=100):
        if (self.moteur_cote == 'l'):
            self.picocar.Car_Run_M1(vitesse)
        else:
            self.picocar.Car_Run_M2(vitesse)
        
    def marcheArriere(self, vitesse=100):
        if (self.moteur_cote == 'l'):
            self.picocar.Car_Back_M1(vitesse)
        else:
            self.picocar.Car_Back_M2(vitesse)
        
    def stop(self):
        if (self.moteur_cote == 'l'):
            self.picocar.Car_Stop_M1()
        else:
            self.picocar.Car_Stop_M2()
    
if __name__ == '__main__':
    print('test classe moteur')
    pico_car = pico_car()
    
    # Initialisation des moteurs
    m1 = Moteur(pico_car,'l')
    m2 = Moteur(pico_car,'r')
    print('le robot avance')    
    m1.marcheAvant()
    m2.marcheAvant()
    time.sleep(1)
    print('le robot s arrete')    
    m1.stop()
    m2.stop()
    
    
