#=====================================================
# Demo Music leds:
# - Joue une musique avec eclairage des touches
# - 3 musiques dispo: au clair de la lune, jingle bells,tetris
#=====================================================
from machine import Pin
from buzzer import Buzzer
from classe_music_P import Music_P
from neopixel import Neopixel
from time import sleep
import time


# on place les couleurs dans un dictionnaire
colors = {"noir":(0,0,0),"blanc":(255,255,255),"vert":(0,255,0),"rouge":(255,0,0),"bleu":(0,0,255),
          "orange":(255,102,0), "jaune":(255,255,0), "violet":(128,0,128)}

led_notes = {"silence":(0,"noir"),
              "do_1":(0,"vert"),"do#_1":(0,"bleu"),
              "re_1":(1,"jaune"),"re#_1":(1,"bleu"),
              "mi_1":(2,"rouge"),
              "fa_1":(3,"bleu"),"fa#_1":(3,"bleu"),
              "sol_1":(4,"vert"),"sol#_1":(4,"bleu"),
              "la_1":(5,"jaune"),"la#_1":(5,"bleu"),
              "si_1":(6,"rouge"),
              "do_2":(0,"vert"),"do#_2":(0,"bleu"),
              "re_2":(1,"bleu"),"re#_2":(1,"bleu"),
              "mi_2":(2,"vert"),
              "fa_2":(3,"jaune"),"fa#_2":(3,"bleu"),
              "sol_2":(4,"vert"),"sol#_2":(4,"bleu"),
              "la_2":(5,"vert"),"la#_2":(5,"bleu"),
              "si_2":(6,"vert"),
              "do_3":(7,"bleu"),"do#_3":(7,"rouge"),
              "re_3":(8,"vert"),"re#_3":(8,"rouge"),
              "mi_3":(9,"jaune"),
              "fa_3":(10,"violet"),"fa#_3":(10,"rouge"),
              "sol_3":(11,"vert"),"sol#_3":(11,"rouge"),
              "la_3":(12,"bleu"),"la#_3":(12,"rouge"),
              "si_3":(13,"violet"),
              "do_4":(7,"rouge"),"do#_4":(7,"rouge"),
              "re_4":(8,"bleu"),"re#_4":(8,"rouge"),
              "mi_4":(9,"jaune"),
              "fa_4":(10,"violet"),"fa#_4":(10,"rouge"),
              "sol_4":(11,"vert"),"sol#_4":(11,"rouge"),
              "la_4":(12,"bleu"),"la#_4":(12,"rouge"),
              "si_4":(13,"jaune"),
              "do_5":(0,"vert"),"do#_5":(0,"bleu"),
              "re_5":(1,"vert"),"re#_5":(1,"bleu"),
              "mi_5":(2,"vert"),
              "fa_5":(3,"vert"),"fa#_5":(3,"bleu"),
              "sol_5":(4,"vert"),"sol#_5":(4,"bleu"),
              "la_5":(5,"vert"),"la#_5":(5,"bleu"),
              "si_5":(6,"vert"),}

# Declaration du buzzer et de la classe music
buz = Buzzer(2)
buz.stop()
music = Music_P(buz)

# Declaration du ruban de leds (Pin 0)
NUMLED =30 #30
leds = Neopixel(NUMLED, 0, 0, "GRB")

# on definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

#melodie = music.Silent_Night
melodie = music.We_Wish_You_a_Merry_Christmas
#melodie = music.Pacman
#melodie = music.Theme_A_from_Tetris_Korobeiniki
#melodie = music.Super_Mario_Bros_theme_by_Koji_Kondo
#melodie = music.The_Legend_of_Zelda_theme
#melodie = music.Star_Wars_theme
#melodie = music.Dart_Vader_theme
#melodie = music.Nokia_Ringtone
#melodie = music.self.La_lettre_a_Elise_Beethoven
#melodie = music.self.Take_on_me_Aha

try:
    print(f"Melodie: {melodie['titre']}")
    music.tempo = melodie["tempo"]
    for note,duree in melodie["notes"]:
        a,c = led_notes[note]
        print(a,c)
        leds.set_pixel(a,colors[c])
        leds.show()
        music.joue_note(note,duree)
        leds.set_pixel(a,colors["noir"])
        leds.show()
    sleep(0.01)
finally:
    buz.stop()

         
         
