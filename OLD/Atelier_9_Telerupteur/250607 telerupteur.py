#Le télérupteur
from machine import Pin
import utime

BP0 = Pin(0, Pin.IN, Pin.PULL_UP) # bouton non appuyé, BP0 a la valeur 1
BP1= Pin(1, Pin.IN, Pin.PULL_UP)
LED = Pin(2, Pin.OUT)

LED.value(0) # on eteint la led pour correspondre à l'état initial

# defintion des etats
Etat_initial = 0  
Etat1_ON= 1  	
Etat2_ON = 2	
Etat3_OFF = 3	

# variable memorisant l'etat courant, etat courant va prendre les valeurs 0,1,2,3
etat_courant = Etat_initial	


# boucle principale
while True:
    # lit la valeur des bp
    bp0_value = BP0.value()
    bp1_value = BP1.value()
    # en fonction de l'etat ou l'on se trouve
    if etat_courant == Etat_initial:	
        # on regarde l'etat des boutons
        # si un est appuyé 1 on effectue l'action
        if bp0_value == 0 or bp1_value == 0 : # bouton appuyé
            print(f"bp0= {BP0.value()},bp1= {BP1.value()}, etat led: {etat_courant}")
            # on allume la led et on change d'etat
            LED.value(1)
            etat_courant = Etat1_ON 
            utime.sleep_ms(150)
            
    elif etat_courant == Etat1_ON:	
        if bp0_value == 1 or bp1_value == 1 :
            print(f"bp0 = {BP0.value()},bp1 = {BP1.value()},état led:  {etat_courant}")
            # on change d'etat sans modifier la led
            etat_courant = Etat2_ON	
            utime.sleep_ms(150)
            
    elif etat_courant == Etat2_ON:	
        if bp0_value == 0 or bp1_value == 0 :
            print(f"bp0 = {BP0.value()},bp1 = {BP1.value()},état led:{etat_courant}")
            # on change d'etat et on eteint la led
            LED.value(0)
            etat_courant = Etat3_OFF
            utime.sleep_ms(150)
            
    elif etat_courant == Etat3_OFF:
        if bp0_value == 1 or bp1_value == 1:
            print(f"bp0 = {BP0.value()},bp1 = {BP1.value()},état led:{etat_courant}")
            # on change d'etat sans modifier la led
            etat_courant = Etat_initial
            utime.sleep_ms(150)


        