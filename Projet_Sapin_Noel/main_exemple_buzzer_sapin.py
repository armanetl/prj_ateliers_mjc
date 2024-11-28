from machine import Pin
from buzzer import Buzzer
from time import sleep

# frequences des notes
freq_notes = {"do":1046,"re":1175,"mi":1318,"fa":1397,"so":1568,"la":1760,"si":1967}

# declaration du buzzer (Pin2, alimentation en 3.3V)
buz = Buzzer(2)
buz.stop()

# fonction qui va jouer une note
def joue_note(val_note,time):
    global buz
    buz.set_freq(freq_notes[val_note])
    buz.start()
    sleep(time)
    buz.stop()


notes = ["mi","mi","mi"   ,"mi","mi","mi" ,"mi","so","do","re"   ,"mi"  ,"fa","fa","fa"   ,"mi","mi","mi"  ,"re","re","re","mi"  ,"re","so"]
duree = [0.25,0.25,0.5    ,0.25,0.25,0.5  ,0.25,0.25,0.25,0.25   ,1     ,0.25,0.25,0.5    ,0.25,0.25,0.5   ,0.25,0.25,0.25,0.25  ,0.5,0.5]
pause = [0.01,0.01,0.01   ,0.01,0.01,0.01 ,0,0,0,0               ,0     ,0.01,0.01,0.01   ,0.01,0.01,0.01  ,0.01,0.01,0,0.01     ,0,0]

notes2 = ["mi","mi","mi"   ,"mi","mi","mi" ,"mi","so","do","re"   ,"mi"  ,"fa","fa","fa"   ,"mi","mi","mi"  ,"so","fa","mi","re"  ,"do"]
duree2 = [0.25,0.25,0.5    ,0.25,0.25,0.5  ,0.25,0.25,0.25,0.25   ,1     ,0.25,0.25,0.5    ,0.25,0.25,0.5   ,0.25,0.25,0.25,0.25  ,1]
pause2 = [0.01,0.01,0.01   ,0.01,0.01,0.01 ,0,0,0,0               ,0     ,0.01,0.01,0.01   ,0.01,0.01,0.01  ,0,0,0,0              ,0]


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
 

  
   
    


