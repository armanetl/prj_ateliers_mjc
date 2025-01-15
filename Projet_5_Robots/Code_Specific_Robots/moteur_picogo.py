from Motor_mjc import PicoGo
import time

        
class Moteur():
    def __init__(self, pico_go, moteur_cote = 'l'):
        self.picogo = pico_go
        self.moteur_cote = moteur_cote

    def marcheAvant(self, vitesse=100):
        if (self.moteur_cote == 'l'):
            self.picogo.forward_M1(vitesse)
        else:
            self.picogo.forward_M2(vitesse)
        
    def marcheArriere(self, vitesse=100):
        if (self.moteur_cote == 'l'):
            self.picogo.backward_M1(vitesse)
        else:
            self.picogo.backward_M2(vitesse)
        
    def stop(self):
        if (self.moteur_cote == 'l'):
            self.picogo.stop_M1()
        else:
            self.picogo.stop_M2()
    
if __name__ == '__main__':
    print('test classe moteur')
    pico_go = PicoGo()
    
    # Initialisation des moteurs
    m1 = Moteur(pico_go,'l')
    m2 = Moteur(pico_go,'r')
    print('le robot avance')    
    m1.marcheAvant()
    m2.marcheAvant()
    time.sleep(1)
    print('le robot s arrete')    
    m1.stop()
    m2.stop()
    
    
