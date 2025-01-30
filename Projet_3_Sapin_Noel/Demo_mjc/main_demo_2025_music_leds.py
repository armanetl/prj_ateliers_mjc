#=====================================================
# Demo Music leds:
# - Joue une musique avec eclairage des touches
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
              "re_1":(0,"jaune"),"re#_1":(0,"bleu"),
              "mi_1":(0,"rouge"),
              "fa_1":(0,"bleu"),"fa#_1":(0,"bleu"),
              "sol_1":(0,"vert"),"sol#_1":(0,"bleu"),
              "la_1":(0,"jaune"),"la#_1":(0,"bleu"),
              "si_1":(0,"rouge"),
              "do_2":(1,"vert"),"do#_2":(1,"bleu"),
              "re_2":(2,"bleu"),"re#_2":(2,"bleu"),
              "mi_2":(3,"vert"),
              "fa_2":(4,"jaune"),"fa#_2":(4,"bleu"),
              "sol_2":(5,"vert"),"sol#_2":(5,"bleu"),
              "la_2":(6,"vert"),"la#_2":(6,"bleu"),
              "si_2":(7,"vert"),
              "do_3":(8,"bleu"),"do#_3":(8,"rouge"),
              "re_3":(9,"vert"),"re#_3":(9,"rouge"),
              "mi_3":(10,"jaune"),
              "fa_3":(11,"violet"),"fa#_3":(11,"rouge"),
              "sol_3":(12,"vert"),"sol#_3":(12,"rouge"),
              "la_3":(13,"bleu"),"la#_3":(13,"rouge"),
              "si_3":(14,"violet"),
              "do_4":(15,"rouge"),"do#_4":(15,"rouge"),
              "re_4":(16,"bleu"),"re#_4":(16,"rouge"),
              "mi_4":(17,"jaune"),
              "fa_4":(18,"violet"),"fa#_4":(18,"rouge"),
              "sol_4":(19,"vert"),"sol#_4":(19,"rouge"),
              "la_4":(20,"bleu"),"la#_4":(20,"rouge"),
              "si_4":(21,"jaune"),
              "do_5":(22,"vert"),"do#_5":(22,"bleu"),
              "re_5":(23,"vert"),"re#_5":(23,"bleu"),
              "mi_5":(24,"vert"),
              "fa_5":(24,"vert"),"fa#_5":(24,"bleu"),
              "sol_5":(24,"vert"),"sol#_5":(24,"bleu"),
              "la_5":(24,"vert"),"la#_5":(24,"bleu"),
              "si_5":(24,"vert"),}

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

def main_demo_2025_music_leds():
    try:
        print(f"Melodie: {melodie['titre']}")
        music.tempo = melodie["tempo"]
        for note,duree in melodie["notes"]:
            a,c = led_notes[note]
            print(a,c)
            #Choix 1
            #leds.set_pixel(a,colors[c])
            #Choix 2
            #for i in range (0,a):
            #    leds.set_pixel(i,colors[c])
            #Choix 3
            for i in range (0,NUMLED):
                leds.set_pixel(i,colors[c])
            leds.show()
            music.joue_note(note,duree)
            leds.set_pixel(a,colors["noir"])
            leds.show()
        sleep(0.01)
    finally:
        buz.stop()

if __name__ == '__main__':
    main_demo_2025_music_leds()         
         
