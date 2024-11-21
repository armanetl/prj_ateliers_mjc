from machine import Pin,PWM
import time
from time import sleep
import _thread

# frequences des notes
freq_notes = {"do":1046,"re":1175,"mi":1318,"fa":1397,"so":1568,"la":1760,"si":1967}

# declaration du buzzer 
buz = PWM(Pin(15))

# fonction qui va jouer une note
def joue_note(val_note,time):
    global buz
    buz.freq(freq_notes[val_note])
    buz.duty_u16(1000) #volume
    sleep(time)


notes = ["mi","mi","mi"   ,"mi","mi","mi" ,"mi","so","do","re"   ,"mi"  ,"fa","fa","fa"   ,"mi","mi","mi"  ,"re","re","re","mi"  ,"re","so"]
duree = [0.25,0.25,0.5    ,0.25,0.25,0.5  ,0.25,0.25,0.25,0.25   ,1     ,0.25,0.25,0.5    ,0.25,0.25,0.5   ,0.25,0.25,0.25,0.25  ,0.5,0.5]
pause = [0.01,0.01,0.01   ,0.01,0.01,0.01 ,0,0,0,0               ,0     ,0.01,0.01,0.01   ,0.01,0.01,0.01  ,0.01,0.01,0,0.01     ,0,0]

notes2 = ["mi","mi","mi"   ,"mi","mi","mi" ,"mi","so","do","re"   ,"mi"  ,"fa","fa","fa"   ,"mi","mi","mi"  ,"so","fa","mi","re"  ,"do"]
duree2 = [0.25,0.25,0.5    ,0.25,0.25,0.5  ,0.25,0.25,0.25,0.25   ,1     ,0.25,0.25,0.5    ,0.25,0.25,0.5   ,0.25,0.25,0.25,0.25  ,1]
pause2 = [0.01,0.01,0.01   ,0.01,0.01,0.01 ,0,0,0,0               ,0     ,0.01,0.01,0.01   ,0.01,0.01,0.01  ,0,0,0,0              ,0]

def task(n, delay):
    while True:
        # joue la partie 1
        index = 0
        for note in notes:
            joue_note(note,duree[index])
            sleep(pause[index])
            index = index+1
        # joue la partie 2
        index = 0
        for note in notes2:
            joue_note(note,duree2[index])
            sleep(pause2[index])
            index = index+1
            
#_thread.start_new_thread(task, (10, 0.5))
task(0,0)


  
   
    


