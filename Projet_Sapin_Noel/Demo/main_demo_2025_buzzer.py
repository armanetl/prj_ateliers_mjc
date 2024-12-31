from machine import Pin
from buzzer import Buzzer
from classe_music_P import Music_P
from time import sleep

button = Pin(22, Pin.IN, Pin.PULL_UP)

buz = Buzzer(2)
buz.stop()
music = Music_P(buz)

#music.joue_melodie(music.jingle)
music.joue_melodie(music.Theme_A_from_Tetris_Korobeiniki)

idx_melodie = -1
print(f"Attends l'appui sur le bouton de selection pour continuer")
while True:

    if button.value()==0: # bouton enfoncé...
        while button.value()==0: # ...on attend qu'il soit relevé
            sleep(0.1)
        idx_melodie+=1 # prochaine chanson
        idx_melodie%=len(music.melodies) # si on arrive à la dernière, on reboucle à la 1ère chanson
    
        melodie=music.melodies[idx_melodie]
        music.joue_melodie(melodie)
    sleep(0.1)
