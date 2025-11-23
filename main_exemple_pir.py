#=====================================================
# Detection simple d'une presence
# Affichage sur la console
#=====================================================
from machine import Pin
from time import sleep


# declaration du detecteur infra rouge
pir_sensor = Pin(16, Pin.IN)

while True:
    reading = pir_sensor.value()
    #si quelquechose a ete detecte
    if reading == 1:
        print("Presence detectée")
    #si rien  n'a ete detecte
    else:
        print("Rien a signaler")
    #on attends 1 seconde    
    sleep(2)

    
   
    


