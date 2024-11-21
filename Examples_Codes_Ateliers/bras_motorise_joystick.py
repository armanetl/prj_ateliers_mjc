# pilotage d'un PanTilt servos SG90 à partir d'un joystick

#initialisation 
from machine import Pin, PWM, ADC
from time import sleep_ms

potX = ADC(26)
potY = ADC(27)

servoX = PWM(Pin(19))
servoY = PWM(Pin(16))
servoX.freq(50) #PWM à 50 hertz soit 20ms de temps de cycle, après il faut faire
# varier le rapport cyclique pour changer l'angle du servo
servoY.freq(50)

# parametres du filtrage pour ne pas osciller lorque l'on est dans une
# position du joystick
deltaval=700
valx= 33000
valy = 33000
#fonction de calcul de la largeur du pulse en fonction des valeurs
#mini et maxi des entrées analogiques et des sorties PWM

def Map(x, in_min, in_max, out_min, out_max):           
    return int((x - in_min)*(out_max-out_min)/(in_max-in_min) + out_min)

  
while True:
    
    #lecture des potentiomètres du joystick
    valX = potX.read_u16()
    valY = potY.read_u16()
    
    if valx-deltaval<valX <valx+deltaval:
        valX=valx
    else :
        pass
    if valy-deltaval<valY<valy+deltaval:
        valY=valy
    else :
        pass
   
    #print('valX =', valX,'valY= ', valY)
    
# suivant le balayage possible mécaniquement, on va fixer
# les bornes du rapport cyclique min, max pour le Pan et le Tilt
    pulseDX = Map(valX, 0, 65535,500000, 1700000)  # Tilt
    pulseDY = Map(valY, 0, 65535,400000, 2500000)   # Pan
    
    #print("pulseDX = ", pulseDX, "pulseDY = ", pulseDY)
    
# commande des servos

    servoX.duty_ns(pulseDX)
    servoY.duty_ns(pulseDY)
    valx=valX
    valy=valY
     
    sleep_ms(100)