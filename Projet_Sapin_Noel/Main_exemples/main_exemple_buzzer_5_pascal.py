'''
melodies = [
     jingle,
     Star_Trek_intro,
     Silent_Night,
     We_Wish_You_a_Merry_Christmas,
     Happy_Birthday,
     Pacman,
     Theme_A_from_Tetris_Korobeiniki,
     Super_Mario_Bros_theme_by_Koji_Kondo,
     The_Legend_of_Zelda_theme,
     At_Dooms_Gate_E1M1,
     Vampire_Killer_Castlevania,
     Star_Wars_theme,
     Dart_Vader_theme,
     Nokia_Ringtone,
     Badinerie_Johann_Sebastian_Bach,
     La_lettre_a_Elise_Beethoven,
     La_panthere_rose,
     Harry_Potter,
     Keyboard_cat,
     Game_of_Thrones,
     Greensleeves,
     Baby_Elephant_Walk,
     Take_on_me_Aha,
     Le_Parrain_theme,
]
'''
from machine import Pin
from buzzer import Buzzer
from time import sleep

pinBuzzer = 2
pinButton = 22
button = Pin(pinButton, Pin.IN, Pin.PULL_UP)

tempo = 140 # sera redéfini pour chaque mélodie

# durée/temps des notes
T = 0.25/2 # triple croche
Tpt = T*1.5 # triple croche pointée
D = 0.25 # double croche
Dpt = D*1.5 # double croche pointée
C = 0.5 # croche
Cpt = 0.75 # croche pointée
N = 1 # noire
Npt = 1.5 # noire pointée
B = 2 # blanche
Bpt = 3 # blanche pointée
R = 4 # ronde
Rpt = 6 # ronde pointée



# frequence note
freq_notes = {"silence":0,
              "do_1":65.41,"do#_1":69.30,
              "re_1":73.42,"re#_1":77.78,
              "mi_1":82.41,
              "fa_1":87.31,"fa#_1":92.50,
              "sol_1":98.00,"sol#_1":103.83,
              "la_1":110.00,"la#_1":116.54,
              "si_1":123.47,
              "do_2":130.81,"do#_2":138.59,
              "re_2":146.83,"re#_2":155.56,
              "mi_2":164.81,
              "fa_2":174.61,"fa#_2":185.00,
              "sol_2":196,"sol#_2":207.65,
              "la_2":220,"la#_2":233.08,
              "si_2":246.94,
              "do_3":261.63,"do#_3":277.18,
              "re_3":293.66,"re#_3":311.13,
              "mi_3":329.63,
              "fa_3":349.23,"fa#_3":369.99,
              "sol_3":392,"sol#_3":415.30,
              "la_3":440,"la#_3":466.16,
              "si_3":493.88,
              "do_4":523.25,"do#_4":554.37,
              "re_4":587.33,"re#_4":622.25,
              "mi_4":659.26,
              "fa_4":698.46,"fa#_4":739.99,
              "sol_4":783.99,"sol#_4":830.61,
              "la_4":880,"la#_4":932.33,
              "si_4":987.77,
              "do_5":1046.50,"do#_5":1108.73,
              "re_5":1174.66,"re#_5":1244.51,
              "mi_5":1318.51,
              "fa_5":1396.91,"fa#_5":1479.98,
              "sol_5":1567.98,"sol#_5":1661.22,
              "la_5":1760.00,"la#_5":1864.66,
              "si_5":1975.53,
              "do_6":2093.00,"do#_6":2217.46,
              "re_6":2349.32,"re#_6":2489.02,
              "mi_6":2637.02,
              "fa_6":2793.83,"fa#_6":2959.96,
              "sol_6":3135.96,"sol#_6":3322.44,
              "la_6":3520.00,"la#_6":3729.31,
              "si_6":3951.07,
              "do_7":4186.01,"do#_7":4434.92,
              "re_7":4698.64,"re#_7":4978.03,
              "mi_7":5274.04,
              "fa_7":5587.65,"fa#_7":5919.91,
              "sol_7":6271.93,"sol#_7":6644.88,
              "la_7":7040.00,"la#_7":7458.62,
              "si_7":7902.13}

#
buz = Buzzer(pinBuzzer)
buz.stop()

#
def joue_note(val_note,time):
    global buz
    if val_note == "silence":
        sleep((60/tempo)*time)
    else:
        buz.set_freq(freq_notes[val_note])
        buz.start()
        sleep((60/tempo)*time)
        buz.stop()

def joue_melodie(melodie):
    try:
        print(f"melodie: {melodie['titre']}")
        tempo = melodie["tempo"]
        for note,duree in melodie["notes"]:
            joue_note(note,duree)
            sleep(0.01)
            
            if button.value()==0: # arrête cette mélodie si le bouton est appuyé
                break
    finally:
        buz.stop()

    
#
jingle = {"titre":"jingle bell",
          "tempo":80,
          "notes":
           [("mi_3",D), ("mi_3",D), ("mi_3",C),
            ("mi_3",D), ("mi_3",D), ("mi_3",C),
            ("mi_3",D), ("sol_3",D), ("do_3",D), ("re_3",D),
            ("mi_3",N),
            ("fa_3",D), ("fa_3",D), ("fa_3",C),
            ("mi_3",D), ("mi_3",D), ("mi_3",C),
            ("re_3",D), ("re_3",D), ("re_3",D), ("mi_3",D),
            ("re_3",C), ("sol_3",C),
            ("mi_3",D), ("mi_3",D), ("mi_3",C),
            ("mi_3",D), ("mi_3",D), ("mi_3",C),
            ("mi_3",D), ("sol_3",D), ("do_3",D), ("re_3",D),
            ("mi_3",N),
            ("fa_3",D), ("fa_3",D), ("fa_3",C),
            ("mi_3",D), ("mi_3",D), ("mi_3",C),
            ("sol_3",D), ("fa_3",D), ("mi_3",D), ("re_3",D),
            ("do_3",N)]
        }

Star_Trek_intro = {'titre':'Star Trek intro', 'tempo':80,
    'notes':[ ('re_3',Cpt),('sol_3',D),('do_4',Npt),('si_3',C),('sol_3',Dpt),('mi_3',Dpt),('la_3',Dpt),('re_4',B),] }
Silent_Night = {'titre':'Silent Night', 'tempo':140,
    'notes':[ ('sol_3',Npt),('la_3',C),('sol_3',N),('mi_3',Bpt),('sol_3',Npt),('la_3',C),('sol_3',N),('mi_3',Bpt),('re_4',B),('re_4',N),('si_3',Bpt),('do_4',B),('do_4',N),('sol_3',Bpt),('la_3',B),('la_3',N),('do_4',Npt),('si_3',C),('la_3',N),('sol_3',Npt),('la_3',C),('sol_3',N),('mi_3',Bpt),('la_3',B),('la_3',N),('do_4',Npt),('si_3',C),('la_3',N),('sol_3',Npt),('la_3',C),('sol_3',N),('mi_3',Bpt),('re_4',B),('re_4',N),('fa_4',Npt),('re_4',C),('si_3',N),('do_4',Bpt),('mi_4',Bpt),('do_4',N),('sol_3',N),('mi_3',N),('sol_3',Npt),('fa_3',C),('re_3',N),('do_3',Bpt),('do_3',Rpt),] }
We_Wish_You_a_Merry_Christmas = {'titre':'We Wish You a Merry Christmas', 'tempo':140,
    'notes':[ ('do_4',N),('fa_4',N),('fa_4',C),('sol_4',C),('fa_4',C),('mi_4',C),('re_4',N),('re_4',N),('re_4',N),('sol_4',N),('sol_4',C),('la_4',C),('sol_4',C),('fa_4',C),('mi_4',N),('do_4',N),('do_4',N),('la_4',N),('la_4',C),('la#_4',C),('la_4',C),('sol_4',C),('fa_4',N),('re_4',N),('do_4',C),('do_4',C),('re_4',N),('sol_4',N),('mi_4',N),('fa_4',B),('do_4',N),('fa_4',N),('fa_4',C),('sol_4',C),('fa_4',C),('mi_4',C),('re_4',N),('re_4',N),('re_4',N),('sol_4',N),('sol_4',C),('la_4',C),('sol_4',C),('fa_4',C),('mi_4',N),('do_4',N),('do_4',N),('la_4',N),('la_4',C),('la#_4',C),('la_4',C),('sol_4',C),('fa_4',N),('re_4',N),('do_4',C),('do_4',C),('re_4',N),('sol_4',N),('mi_4',N),('fa_4',B),('do_4',N),('fa_4',N),('fa_4',N),('fa_4',N),('mi_4',B),('mi_4',N),('fa_4',N),('mi_4',N),('re_4',N),('do_4',B),('la_4',N),('la#_4',N),('la_4',N),('sol_4',N),('do_5',N),('do_4',N),('do_4',C),('do_4',C),('re_4',N),('sol_4',N),('mi_4',N),('fa_4',B),('do_4',N),('fa_4',N),('fa_4',C),('sol_4',C),('fa_4',C),('mi_4',C),('re_4',N),('re_4',N),('re_4',N),('sol_4',N),('sol_4',C),('la_4',C),('sol_4',C),('fa_4',C),('mi_4',N),('do_4',N),('do_4',N),('la_4',N),('la_4',C),('la#_4',C),('la_4',C),('sol_4',C),('fa_4',N),('re_4',N),('do_4',C),('do_4',C),('re_4',N),('sol_4',N),('mi_4',N),('fa_4',B),('do_4',N),('fa_4',N),('fa_4',N),('fa_4',N),('mi_4',B),('mi_4',N),('fa_4',N),('mi_4',N),('re_4',N),('do_4',B),('la_4',N),('la#_4',N),('la_4',N),('sol_4',N),('do_5',N),('do_4',N),('do_4',C),('do_4',C),('re_4',N),('sol_4',N),('mi_4',N),('fa_4',B),('do_4',N),('fa_4',N),('fa_4',C),('sol_4',C),('fa_4',C),('mi_4',C),('re_4',N),('re_4',N),('re_4',N),('sol_4',N),('sol_4',C),('la_4',C),('sol_4',C),('fa_4',C),('mi_4',N),('do_4',N),('do_4',N),('la_4',N),('la_4',C),('la#_4',C),('la_4',C),('sol_4',C),('fa_4',N),('re_4',N),('do_4',C),('do_4',C),('re_4',N),('sol_4',N),('mi_4',N),('fa_4',B),('do_4',N),('fa_4',N),('fa_4',C),('sol_4',C),('fa_4',C),('mi_4',C),('re_4',N),('re_4',N),('re_4',N),('sol_4',N),('sol_4',C),('la_4',C),('sol_4',C),('fa_4',C),('mi_4',N),('do_4',N),('do_4',N),('la_4',N),('la_4',C),('la#_4',C),('la_4',C),('sol_4',C),('fa_4',N),('re_4',N),('do_4',C),('do_4',C),('re_4',N),('sol_4',N),('mi_4',N),('fa_4',B),('silence',N),] }
Happy_Birthday = {'titre':'Happy Birthday', 'tempo':140,
    'notes':[ ('do_3',N),('do_3',C),('re_3',Npt),('do_3',Npt),('fa_3',Npt),('mi_3',Bpt),('do_3',N),('do_3',C),('re_3',Npt),('do_3',Npt),('sol_3',Npt),('fa_3',Bpt),('do_3',N),('do_3',C),('do_4',Npt),('la_3',Npt),('fa_3',Npt),('mi_3',Npt),('re_3',Npt),('la#_3',N),('la#_3',C),('la_3',Npt),('fa_3',Npt),('sol_3',Npt),('fa_3',Bpt),] }
Pacman = {'titre':'Pacman', 'tempo':105,
    'notes':[ ('si_3',D),('si_4',D),('fa#_4',D),('re#_4',D),('si_4',T),('fa#_4',Dpt),('re#_4',C),('do_4',D),('do_5',D),('sol_5',D),('mi_5',D),('do_5',T),('sol_5',Dpt),('mi_5',C),('si_3',D),('si_4',D),('fa#_4',D),('re#_4',D),('si_4',T),('fa#_4',Dpt),('re#_4',C),('re#_4',T),('mi_4',T),('fa_4',T),('fa_4',T),('fa#_4',T),('sol_4',T),('sol_4',T),('sol#_4',T),('la_4',D),('si_4',C),] }
Theme_A_from_Tetris_Korobeiniki = {'titre':'Theme A from Tetris (Korobeiniki)', 'tempo':144,
    'notes':[ ('mi_4',N),('si_3',C),('do_4',C),('re_4',N),('do_4',C),('si_3',C),('la_3',N),('la_3',C),('do_4',C),('mi_4',N),('re_4',C),('do_4',C),('si_3',Npt),('do_4',C),('re_4',N),('mi_4',N),('do_4',N),('la_3',N),('la_3',C),('la_3',N),('si_3',C),('do_4',C),('re_4',Npt),('fa_4',C),('la_4',N),('sol_4',C),('fa_4',C),('mi_4',Npt),('do_4',C),('mi_4',N),('re_4',C),('do_4',C),('si_3',N),('si_3',C),('do_4',C),('re_4',N),('mi_4',N),('do_4',N),('la_3',N),('la_3',N),('silence',N),('mi_4',N),('si_3',C),('do_4',C),('re_4',N),('do_4',C),('si_3',C),('la_3',N),('la_3',C),('do_4',C),('mi_4',N),('re_4',C),('do_4',C),('si_3',Npt),('do_4',C),('re_4',N),('mi_4',N),('do_4',N),('la_3',N),('la_3',C),('la_3',N),('si_3',C),('do_4',C),('re_4',Npt),('fa_4',C),('la_4',N),('sol_4',C),('fa_4',C),('mi_4',Npt),('do_4',C),('mi_4',N),('re_4',C),('do_4',C),('si_3',N),('si_3',C),('do_4',C),('re_4',N),('mi_4',N),('do_4',N),('la_3',N),('la_3',N),('silence',N),('mi_4',B),('do_4',B),('re_4',B),('si_3',B),('do_4',B),('la_3',B),('sol#_3',B),('si_3',N),('silence',C),('mi_4',B),('do_4',B),('re_4',B),('si_3',B),('do_4',N),('mi_4',N),('la_4',B),('sol#_4',B),] }
Super_Mario_Bros_theme_by_Koji_Kondo = {'titre':'Super Mario Bros theme, by Koji Kondo', 'tempo':200,
    'notes':[ ('mi_4',C),('mi_4',C),('silence',C),('mi_4',C),('silence',C),('do_4',C),('mi_4',C),('sol_4',N),('silence',N),('sol_3',C),('silence',N),('do_4',Npt),('sol_3',C),('silence',N),('mi_3',Npt),('la_3',N),('si_3',N),('la#_3',C),('la_3',N),('sol_3',Cpt),('mi_4',Cpt),('sol_4',Cpt),('la_4',N),('fa_4',C),('sol_4',C),('silence',C),('mi_4',N),('do_4',C),('re_4',C),('si_3',Npt),('do_4',Npt),('sol_3',C),('silence',N),('mi_3',Npt),('la_3',N),('si_3',N),('la#_3',C),('la_3',N),('sol_3',Cpt),('mi_4',Cpt),('sol_4',Cpt),('la_4',N),('fa_4',C),('sol_4',C),('silence',C),('mi_4',N),('do_4',C),('re_4',C),('si_3',Npt),('silence',N),('sol_4',C),('fa#_4',C),('fa_4',C),('re#_4',N),('mi_4',C),('silence',C),('sol#_3',C),('la_3',C),('do_3',C),('silence',C),('la_3',C),('do_4',C),('re_4',C),('silence',N),('re#_4',N),('silence',C),('re_4',Npt),('do_4',B),('silence',B),('silence',N),('sol_4',C),('fa#_4',C),('fa_4',C),('re#_4',N),('mi_4',C),('silence',C),('sol#_3',C),('la_3',C),('do_3',C),('silence',C),('la_3',C),('do_4',C),('re_4',C),('silence',N),('re#_4',N),('silence',C),('re_4',Npt),('do_4',B),('silence',B),('do_4',C),('do_4',N),('do_4',C),('silence',C),('do_4',C),('re_4',N),('mi_4',C),('do_4',N),('la_3',C),('sol_3',B),('do_4',C),('do_4',N),('do_4',C),('silence',C),('do_4',C),('re_4',C),('mi_4',C),('silence',R),('do_4',C),('do_4',N),('do_4',C),('silence',C),('do_4',C),('re_4',N),('mi_4',C),('do_4',N),('la_3',C),('sol_3',B),('mi_4',C),('mi_4',C),('silence',C),('mi_4',C),('silence',C),('do_4',C),('mi_4',N),('sol_4',N),('silence',N),('sol_3',N),('silence',N),('do_4',Npt),('sol_3',C),('silence',N),('mi_3',Npt),('la_3',N),('si_3',N),('la#_3',C),('la_3',N),('sol_3',Cpt),('mi_4',Cpt),('sol_4',Cpt),('la_4',N),('fa_4',C),('sol_4',C),('silence',C),('mi_4',N),('do_4',C),('re_4',C),('si_3',Npt),('do_4',Npt),('sol_3',C),('silence',N),('mi_3',Npt),('la_3',N),('si_3',N),('la#_3',C),('la_3',N),('sol_3',Cpt),('mi_4',Cpt),('sol_4',Cpt),('la_4',N),('fa_4',C),('sol_4',C),('silence',C),('mi_4',N),('do_4',C),('re_4',C),('si_3',Npt),('mi_4',C),('do_4',N),('sol_3',C),('silence',N),('sol#_3',N),('la_3',C),('fa_4',N),('fa_4',C),('la_3',B),('re_4',Cpt),('la_4',Cpt),('la_4',Cpt),('la_4',Cpt),('sol_4',Cpt),('fa_4',Cpt),('mi_4',C),('do_4',N),('la_3',C),('sol_3',B),('mi_4',C),('do_4',N),('sol_3',C),('silence',N),('sol#_3',N),('la_3',C),('fa_4',N),('fa_4',C),('la_3',B),('si_3',C),('fa_4',N),('fa_4',C),('fa_4',Cpt),('mi_4',Cpt),('re_4',Cpt),('do_4',C),('mi_3',N),('mi_3',C),('do_3',B),('mi_4',C),('do_4',N),('sol_3',C),('silence',N),('sol#_3',N),('la_3',C),('fa_4',N),('fa_4',C),('la_3',B),('re_4',Cpt),('la_4',Cpt),('la_4',Cpt),('la_4',Cpt),('sol_4',Cpt),('fa_4',Cpt),('mi_4',C),('do_4',N),('la_3',C),('sol_3',B),('mi_4',C),('do_4',N),('sol_3',C),('silence',N),('sol#_3',N),('la_3',C),('fa_4',N),('fa_4',C),('la_3',B),('si_3',C),('fa_4',N),('fa_4',C),('fa_4',Cpt),('mi_4',Cpt),('re_4',Cpt),('do_4',C),('mi_3',N),('mi_3',C),('do_3',B),('do_4',C),('do_4',N),('do_4',C),('silence',C),('do_4',C),('re_4',C),('mi_4',C),('silence',R),('do_4',C),('do_4',N),('do_4',C),('silence',C),('do_4',C),('re_4',N),('mi_4',C),('do_4',N),('la_3',C),('sol_3',B),('mi_4',C),('mi_4',C),('silence',C),('mi_4',C),('silence',C),('do_4',C),('mi_4',N),('sol_4',N),('silence',N),('sol_3',N),('silence',N),('mi_4',C),('do_4',N),('sol_3',C),('silence',N),('sol#_3',N),('la_3',C),('fa_4',N),('fa_4',C),('la_3',B),('re_4',Cpt),('la_4',Cpt),('la_4',Cpt),('la_4',Cpt),('sol_4',Cpt),('fa_4',Cpt),('mi_4',C),('do_4',N),('la_3',C),('sol_3',B),('mi_4',C),('do_4',N),('sol_3',C),('silence',N),('sol#_3',N),('la_3',C),('fa_4',N),('fa_4',C),('la_3',B),('si_3',C),('fa_4',N),('fa_4',C),('fa_4',Cpt),('mi_4',Cpt),('re_4',Cpt),('do_4',C),('mi_3',N),('mi_3',C),('do_3',B),('do_4',Npt),('sol_3',Npt),('mi_3',N),('la_3',Cpt),('si_3',Cpt),('la_3',Cpt),('sol#_3',Cpt),('la#_3',Cpt),('sol#_3',Cpt),('sol_3',C),('re_3',C),('mi_3',Bpt),] }
The_Legend_of_Zelda_theme = {'titre':'The Legend of Zelda theme', 'tempo':88,
    'notes':[ ('la#_3',Bpt),('fa_3',C),('fa_3',C),('la#_3',C),('sol#_3',D),('fa#_3',D),('sol#_3',Bpt),('la#_3',Bpt),('fa#_3',C),('fa#_3',C),('la#_3',C),('la_3',D),('sol_3',D),('la_3',Bpt),('silence',R),('la#_3',N),('fa_3',Npt),('la#_3',C),('la#_3',D),('do_4',D),('re_4',D),('re#_4',D),('fa_4',B),('fa_4',C),('fa_4',C),('fa_4',C),('fa#_4',D),('sol#_4',D),('la#_4',Bpt),('la#_4',C),('la#_4',C),('sol#_4',C),('fa#_4',D),('sol#_4',Cpt),('fa#_4',D),('fa_4',B),('fa_4',N),('re#_4',Cpt),('fa_4',D),('fa#_4',B),('fa_4',C),('re#_4',C),('do#_4',Cpt),('re#_4',D),('fa_4',B),('re#_4',C),('do#_4',C),('do_4',Cpt),('re_4',D),('mi_4',B),('sol_4',C),('fa_4',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',C),('fa_3',D),('fa_3',C),('la#_3',N),('fa_3',Npt),('la#_3',C),('la#_3',D),('do_4',D),('re_4',D),('re#_4',D),('fa_4',B),('fa_4',C),('fa_4',C),('fa_4',C),('fa#_4',D),('sol#_4',D),('la#_4',Bpt),('do#_5',N),('do_5',N),('la_4',B),('fa_4',N),('fa#_4',Bpt),('la#_4',N),('la_4',N),('fa_4',B),('fa_4',N),('fa#_4',Bpt),('la#_4',N),('la_4',N),('fa_4',B),('re_4',N),('re#_4',Bpt),('fa#_4',N),('fa_4',N),('do#_4',B),('la#_3',N),('do_4',Cpt),('re_4',D),('mi_4',B),('sol_4',C),('fa_4',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',D),('fa_3',C),('fa_3',D),('fa_3',C),] }
At_Dooms_Gate_E1M1 = {'titre':'At Doom\'s Gate (E1M1)', 'tempo':225,
    'notes':[ ('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('fa#_2',Dpt),('re_2',Dpt),('si_1',Dpt),('la_2',Dpt),('fa#_2',Dpt),('si_1',Dpt),('re_2',Dpt),('fa#_2',Dpt),('la_2',Dpt),('fa#_2',Dpt),('re_2',Dpt),('si_1',Dpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('si_2',Dpt),('sol_2',Dpt),('mi_2',Dpt),('sol_2',Dpt),('si_2',Dpt),('mi_3',Dpt),('sol_2',Dpt),('si_2',Dpt),('mi_3',Dpt),('si_2',Dpt),('sol_3',Dpt),('si_3',Dpt),('la_1',C),('la_1',C),('la_2',C),('la_1',C),('la_1',C),('sol_2',C),('la_1',C),('la_1',C),('fa_2',C),('la_1',C),('la_1',C),('re#_2',C),('la_1',C),('la_1',C),('mi_2',C),('fa_2',C),('la_1',C),('la_1',C),('la_2',C),('la_1',C),('la_1',C),('sol_2',C),('la_1',C),('la_1',C),('fa_2',C),('la_1',C),('la_1',C),('re#_2',Bpt),('la_1',C),('la_1',C),('la_2',C),('la_1',C),('la_1',C),('sol_2',C),('la_1',C),('la_1',C),('fa_2',C),('la_1',C),('la_1',C),('re#_2',C),('la_1',C),('la_1',C),('mi_2',C),('fa_2',C),('la_1',C),('la_1',C),('la_2',C),('la_1',C),('la_1',C),('sol_2',C),('la_1',C),('la_1',C),('la_2',Dpt),('fa_2',Dpt),('re_2',Dpt),('la_2',Dpt),('fa_2',Dpt),('re_2',Dpt),('do_3',Dpt),('la_2',Dpt),('fa_2',Dpt),('la_2',Dpt),('fa_2',Dpt),('re_2',Dpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('do#_2',C),('do#_2',C),('do#_3',C),('do#_2',C),('do#_2',C),('si_2',C),('do#_2',C),('do#_2',C),('la_2',C),('do#_2',C),('do#_2',C),('sol_2',C),('do#_2',C),('do#_2',C),('sol#_2',C),('la_2',C),('si_1',C),('si_1',C),('si_2',C),('si_1',C),('si_1',C),('la_2',C),('si_1',C),('si_1',C),('sol_2',C),('si_1',C),('si_1',C),('fa_2',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('si_2',Dpt),('sol_2',Dpt),('mi_2',Dpt),('sol_2',Dpt),('si_2',Dpt),('mi_3',Dpt),('sol_2',Dpt),('si_2',Dpt),('mi_3',Dpt),('si_2',Dpt),('sol_3',Dpt),('si_3',Dpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('fa#_2',Dpt),('re#_2',Dpt),('si_1',Dpt),('fa#_2',Dpt),('re#_2',Dpt),('si_1',Dpt),('sol_2',Dpt),('re_2',Dpt),('si_1',Dpt),('re#_3',Dpt),('re#_2',Dpt),('si_1',Dpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('mi_3',Dpt),('si_2',Dpt),('sol_2',Dpt),('sol_3',Dpt),('mi_3',Dpt),('sol_2',Dpt),('si_2',Dpt),('re_3',Dpt),('mi_3',Dpt),('sol_3',Dpt),('mi_3',Dpt),('sol_2',Dpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('la_1',C),('la_1',C),('la_2',C),('la_1',C),('la_1',C),('sol_2',C),('la_1',C),('la_1',C),('fa_2',C),('la_1',C),('la_1',C),('re#_2',C),('la_1',C),('la_1',C),('mi_2',C),('fa_2',C),('la_1',C),('la_1',C),('la_2',C),('la_1',C),('la_1',C),('sol_2',C),('la_1',C),('la_1',C),('la_2',Dpt),('fa_2',Dpt),('re_2',Dpt),('la_2',Dpt),('fa_2',Dpt),('re_2',Dpt),('do_3',Dpt),('la_2',Dpt),('fa_2',Dpt),('la_2',Dpt),('fa_2',Dpt),('re_2',Dpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',Bpt),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('do_2',C),('mi_1',C),('mi_1',C),('la#_1',C),('mi_1',C),('mi_1',C),('si_1',C),('do_2',C),('mi_1',C),('mi_1',C),('mi_2',C),('mi_1',C),('mi_1',C),('re_2',C),('mi_1',C),('mi_1',C),('si_2',Dpt),('sol_2',Dpt),('mi_2',Dpt),('si_1',Dpt),('mi_2',Dpt),('sol_2',Dpt),('do_3',Dpt),('si_2',Dpt),('sol_2',Dpt),('si_2',Dpt),('sol_2',Dpt),('mi_2',Dpt),] }
Vampire_Killer_Castlevania = {'titre':'Vampire Killer (Castlevania)', 'tempo':130,
    'notes':[ ('mi_4',D),('mi_4',C),('re_4',D),('silence',D),('do#_4',Npt),('mi_3',C),('fa#_3',D),('sol_3',D),('la_3',D),('si_3',Cpt),('mi_3',Cpt),('si_3',C),('la_3',D),('re_4',Npt),('mi_4',D),('mi_4',C),('re_4',D),('silence',D),('do#_4',Npt),('mi_3',C),('fa#_3',D),('sol_3',D),('la_3',D),('si_3',Cpt),('mi_3',Cpt),('si_3',C),('la_3',D),('re_3',Npt),('silence',C),('mi_4',C),('silence',D),('si_4',D),('silence',C),('la#_4',D),('si_4',D),('la#_4',D),('sol_4',D),('silence',N),('si_4',C),('si_4',D),('la#_4',D),('silence',D),('la#_4',D),('la_4',D),('silence',D),('si_4',D),('sol_4',D),('si_4',D),('la#_4',D),('silence',D),('si_4',D),('la_4',D),('sol_4',D),('silence',C),('mi_4',C),('silence',D),('si_4',D),('silence',C),('la#_4',D),('si_4',D),('la#_4',D),('sol_4',D),('silence',N),('si_4',C),('si_4',D),('la#_4',D),('silence',D),('la#_4',D),('la_4',D),('silence',D),('si_4',D),('sol_4',D),('si_4',D),('la#_4',D),('silence',D),('si_4',D),('la_4',D),('sol_4',D),('re#_3',Cpt),('fa#_3',Cpt),('do_4',C),('si_3',Cpt),('sol_3',Cpt),('mi_3',C),('re#_3',Cpt),('fa#_3',Cpt),('do_4',C),('si_3',Cpt),('sol_3',Cpt),('silence',C),('re#_3',Cpt),('fa#_3',Cpt),('do_4',C),('si_3',Cpt),('sol_3',Cpt),('mi_3',C),('re#_3',Cpt),('fa#_3',Cpt),('do_4',C),('si_3',Cpt),('do#_4',Cpt),('re#_4',C),('mi_4',D),('mi_4',D),('mi_3',D),('mi_3',Bpt),('do_3',C),('do_3',C),('mi_3',D),('sol_3',Cpt),('re_3',C),('re_3',C),('fa#_3',D),('la_3',Cpt),('mi_4',D),('mi_4',D),('mi_3',D),('mi_3',Bpt),('do_3',C),('do_3',C),('mi_3',D),('sol_3',Cpt),('re_3',C),('re_3',C),('si_2',D),('re_3',Cpt),('mi_4',D),('mi_4',C),('re_4',D),('silence',D),('do#_4',Npt),('mi_3',C),('fa#_3',D),('sol_3',D),('la_3',D),('si_3',Cpt),('mi_3',Cpt),('si_3',C),('la_3',D),('re_4',Npt),('mi_4',D),('mi_4',C),('re_4',D),('silence',D),('do#_4',Npt),('mi_3',C),('fa#_3',D),('sol_3',D),('la_3',D),('si_3',Cpt),('mi_3',Cpt),('si_3',C),('la_3',D),('re_3',Npt),('silence',C),('mi_4',C),('silence',D),('si_4',D),('silence',C),('la#_4',D),('si_4',D),('la#_4',D),('sol_4',D),('silence',N),('si_4',C),('si_4',D),('la#_4',D),('silence',D),('la#_4',D),('la_4',D),('silence',D),('si_4',D),('sol_4',D),('si_4',D),('la#_4',D),('silence',D),('si_4',D),('la_4',D),('sol_4',D),('silence',C),('mi_4',C),('silence',D),('si_4',D),('silence',C),('la#_4',D),('si_4',D),('la#_4',D),('sol_4',D),('silence',N),('si_4',C),('si_4',D),('la#_4',D),('silence',D),('la#_4',D),('la_4',D),('silence',D),('si_4',D),('sol_4',D),('si_4',D),('la#_4',D),('silence',D),('si_4',D),('la_4',D),('sol_4',D),('re#_3',Cpt),('fa#_3',Cpt),('do_4',C),('si_3',Cpt),('sol_3',Cpt),('mi_3',C),('re#_3',Cpt),('fa#_3',Cpt),('do_4',C),('si_3',Cpt),('sol_3',Cpt),('silence',C),('re#_3',Cpt),('fa#_3',Cpt),('do_4',C),('si_3',Cpt),('sol_3',Cpt),('mi_3',C),('re#_3',Cpt),('fa#_3',Cpt),('do_4',C),('si_3',Cpt),('do#_4',Cpt),('re#_4',C),('mi_4',D),('mi_4',D),('mi_3',D),('mi_3',Bpt),('do_3',C),('do_3',C),('mi_3',D),('sol_3',Cpt),('re_3',C),('re_3',C),('fa#_3',D),('la_3',Cpt),('mi_4',D),('mi_4',D),('mi_3',D),('mi_3',Bpt),('do_3',C),('do_3',C),('mi_3',D),('sol_3',Cpt),('re_3',C),('re_3',C),('si_2',D),('re_3',Cpt),] }
Star_Wars_theme = {'titre':'Star Wars theme', 'tempo':120, #108
    'notes':[ ('la#_3',C),('la#_3',C),('la#_3',C),('fa_4',B),('do_5',B),('la#_4',C),('la_4',C),('sol_4',C),('fa_5',B),('do_5',N),('la#_4',C),('la_4',C),('sol_4',C),('fa_5',B),('do_5',N),('la#_4',C),('la_4',C),('la#_4',C),('sol_4',B),('do_4',C),('do_4',C),('do_4',C),('fa_4',B),('do_5',B),('la#_4',C),('la_4',C),('sol_4',C),('fa_5',B),('do_5',N),('la#_4',C),('la_4',C),('sol_4',C),('fa_5',B),('do_5',N),('la#_4',C),('la_4',C),('la#_4',C),('sol_4',B),('do_4',Cpt),('do_4',D),('re_4',Npt),('re_4',C),('la#_4',C),('la_4',C),('sol_4',C),('fa_4',C),('fa_4',C),('sol_4',C),('la_4',C),('sol_4',N),('re_4',C),('mi_4',N),('do_4',Cpt),('do_4',D),('re_4',Npt),('re_4',C),('la#_4',C),('la_4',C),('sol_4',C),('fa_4',C),('do_5',Cpt),('sol_4',D),('sol_4',B),('silence',C),('do_4',C),('re_4',Npt),('re_4',C),('la#_4',C),('la_4',C),('sol_4',C),('fa_4',C),('fa_4',C),('sol_4',C),('la_4',C),('sol_4',N),('re_4',C),('mi_4',N),('do_5',Cpt),('do_5',D),('fa_5',N),('re#_5',C),('do#_5',N),('do_5',C),('la#_4',N),('sol#_4',C),('sol_4',N),('fa_4',C),('do_5',R),] }
Dart_Vader_theme = {'titre':'Dart Vader theme', 'tempo':120,
    'notes':[ ('la_3',Npt),('la_3',Npt),('la_3',D),('la_3',D),('la_3',D),('la_3',D),('fa_3',C),('silence',C),('la_3',Npt),('la_3',Npt),('la_3',D),('la_3',D),('la_3',D),('la_3',D),('fa_3',C),('silence',C),('la_3',N),('la_3',N),('la_3',N),('fa_3',Cpt),('do_4',D),('la_3',N),('fa_3',Cpt),('do_4',D),('la_3',B),('mi_4',N),('mi_4',N),('mi_4',N),('fa_4',Cpt),('do_4',D),('la_3',N),('fa_3',Cpt),('do_4',D),('la_3',B),('la_4',N),('la_3',Cpt),('la_3',D),('la_4',N),('sol#_4',Cpt),('sol_4',D),('re#_4',D),('re_4',D),('re#_4',C),('silence',C),('la_3',C),('re#_4',N),('re_4',Cpt),('do#_4',D),('do_4',D),('si_3',D),('do_4',D),('silence',C),('fa_3',C),('sol#_3',N),('fa_3',Cpt),('la_3',Dpt),('do_4',N),('la_3',Cpt),('do_4',D),('mi_4',B),('la_4',N),('la_3',Cpt),('la_3',D),('la_4',N),('sol#_4',Cpt),('sol_4',D),('re#_4',D),('re_4',D),('re#_4',C),('silence',C),('la_3',C),('re#_4',N),('re_4',Cpt),('do#_4',D),('do_4',D),('si_3',D),('do_4',D),('silence',C),('fa_3',C),('sol#_3',N),('fa_3',Cpt),('la_3',Dpt),('la_3',N),('fa_3',Cpt),('do_4',D),('la_3',B),] }
Nokia_Ringtone = {'titre':'Nokia Ringtone', 'tempo':180,
    'notes':[ ('mi_4',C),('re_4',C),('fa#_3',N),('sol#_3',N),('do#_4',C),('si_3',C),('re_3',N),('mi_3',N),('si_3',C),('la_3',C),('do#_3',N),('mi_3',N),('la_3',B),] }
Badinerie_Johann_Sebastian_Bach = {'titre':'Badinerie - Johann Sebastian Bach', 'tempo':120,
    'notes':[ ('si_4',Cpt),('re_5',D),('si_4',D),('fa#_4',Cpt),('si_4',D),('fa#_4',D),('re_4',Cpt),('fa#_4',D),('re_4',D),('si_3',N),('fa_3',D),('si_3',D),('re_4',D),('si_3',D),('do#_4',D),('si_3',D),('do#_4',D),('si_3',D),('la#_3',D),('do#_4',D),('mi_4',D),('do#_4',D),('re_4',C),('si_3',C),('si_4',Cpt),('re_5',D),('si_4',D),('fa#_4',Cpt),('si_4',D),('fa#_4',D),('re_4',Cpt),('fa#_4',D),('re_4',D),('si_3',N),('re_4',D),('do#_4',Dpt),('re_4',Cpt),('re_4',D),('do#_4',Dpt),('re_4',Cpt),('si_4',Cpt),('re_4',Cpt),('re_4',C),('do#_4',Cpt),('fa#_4',Dpt),('fa_4',D),('fa#_4',Cpt),('fa#_4',Dpt),('fa_4',D),('fa#_4',Cpt),('re_5',Cpt),('fa#_4',Cpt),('fa#_4',C),('fa_4',C),('do#_4',D),('fa#_4',D),('la_4',D),('fa#_4',D),('sol#_4',D),('fa#_4',D),('sol#_4',D),('fa#_4',D),('fa_4',D),('sol_4',D),('si_4',D),('sol_4',D),('la_4',D),('sol#_4',D),('la_4',D),('sol_4',D),('fa_4',D),('la_4',D),('fa#_4',D),('fa_4',D),('fa#_4',D),('si_4',D),('fa#_4',D),('fa_4',D),('fa#_4',D),('do_5',D),('fa#_4',D),('mi_4',D),('fa#_4',D),('re_5',D),('fa#_4',D),('fa_4',D),('fa#_4',D),('re_5',D),('do_5',D),('si_4',D),('do_5',D),('la_4',D),('sol#_4',D),('fa#_4',D),('la_4',C),('sol_4',C),('fa#_4',N),('silence',N),('fa#_4',Cpt),('la_4',D),('fa#_4',D),('do#_4',Npt),('fa#_4',D),('do#_4',D),('la_3',Cpt),('do#_4',D),('la_3',D),('fa_3',N),('do_4',C),('si_3',C),('mi_4',C),('re#_4',D),('fa#_4',D),('la_4',C),('sol#_4',D),('fa#_4',D),('sol#_4',C),('re_4',C),('sol#_4',Cpt),('si_4',D),('sol#_4',C),('mi_4',Cpt),('sol#_4',D),('mi_4',D),('do#_4',Cpt),('mi_4',D),('do#_4',D),('la_3',N),('la_3',D),('re_4',D),('fa#_4',D),('re_4',D),('mi_4',D),('re_4',D),('mi_4',D),('re_4',D),('do#_4',D),('mi_4',D),('sol_4',D),('mi_4',D),('fa#_4',D),('mi_4',D),('fa#_4',D),('mi_4',D),('re_4',D),('fa#_4',D),('re_4',D),('do#_4',D),('re_4',D),('sol_4',D),('re_4',D),('do#_4',D),('re_4',D),('la_4',D),('re_4',D),('do#_4',D),('re_4',D),('si_4',D),('re_4',D),('do#_4',D),('re_4',D),('si_4',D),('la_4',D),('sol_4',D),('la_4',D),('fa#_4',D),('mi_4',D),('re_4',D),('fa#_4',C),('mi_4',D),('re_4',N),('fa#_4',D),('mi_4',D),('fa#_4',Cpt),('fa#_4',D),('mi_4',D),('fa#_4',Cpt),('re_5',Cpt),('fa#_4',Cpt),('fa#_4',C),('mi_4',C),('mi_4',D),('re_4',D),('mi_4',Cpt),('mi_4',D),('re_4',D),('mi_4',Cpt),('re_5',Cpt),('mi_4',Cpt),('mi_4',C),('re_4',C),('si_4',Cpt),('re_5',D),('si_4',D),('si_4',C),('sol_4',N),('sol_4',N),('si_4',T),('la_4',T),('sol_4',T),('fa#_4',T),('mi_4',N),('mi_4',C),('sol_4',T),('fa#_4',T),('mi_4',T),('re_4',T),('do_4',D),('mi_4',D),('sol_4',D),('mi_4',D),('do#_4',D),('si_3',D),('do#_4',D),('la_3',D),('la#_3',Cpt),('la_3',Cpt),('sol_3',C),('fa_3',C),('la_3',C),('la#_3',D),('do#_4',D),('mi_4',C),('re_4',D),('do#_4',D),('re_4',C),('si_3',T),('do#_4',T),('re_4',T),('mi_4',T),('fa#_4',C),('re_4',D),('fa#_4',D),('si_4',C),('fa#_4',C),('mi_4',D),('re_4',D),('do#_4',D),('re_4',D),('do#_4',C),('si_3',N),] }
La_lettre_a_Elise_Beethoven = {'titre':'Fur Elise - Ludwig van Beethoven', 'tempo':80,
    'notes':[ ('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',Cpt),('do_3',D),('mi_3',D),('la_3',D),('si_3',Cpt),('mi_3',D),('sol#_3',D),('si_3',D),('do_4',C),('silence',D),('mi_3',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',Cpt),('do_3',D),('mi_3',D),('la_3',D),('si_3',Cpt),('mi_3',D),('do_4',D),('si_3',D),('la_3',N),('silence',C),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',Cpt),('do_3',D),('mi_3',D),('la_3',D),('si_3',Cpt),('mi_3',D),('sol#_3',D),('si_3',D),('do_4',C),('silence',D),('mi_3',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',Cpt),('do_3',D),('mi_3',D),('la_3',D),('si_3',Cpt),('mi_3',D),('do_4',D),('si_3',D),('la_3',C),('silence',D),('si_3',D),('do_4',D),('re_4',D),('mi_4',Cpt),('sol_3',D),('fa_4',D),('mi_4',D),('re_4',Cpt),('fa_3',D),('mi_4',D),('re_4',D),('do_4',Cpt),('mi_3',D),('re_4',D),('do_4',D),('si_3',C),('silence',D),('mi_3',D),('mi_4',D),('silence',D),('silence',D),('mi_4',D),('mi_5',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',C),('silence',D),('do_3',D),('mi_3',D),('la_3',D),('si_3',C),('silence',D),('mi_3',D),('sol#_3',D),('si_3',D),('do_4',C),('silence',D),('mi_3',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',C),('silence',D),('do_3',D),('mi_3',D),('la_3',D),('si_3',C),('silence',D),('mi_3',D),('do_4',D),('si_3',D),('la_3',C),('silence',D),('si_3',D),('do_4',D),('re_4',D),('mi_4',Cpt),('sol_3',D),('fa_4',D),('mi_4',D),('re_4',Cpt),('fa_3',D),('mi_4',D),('re_4',D),('do_4',Cpt),('mi_3',D),('re_4',D),('do_4',D),('si_3',C),('silence',D),('mi_3',D),('mi_4',D),('silence',D),('silence',D),('mi_4',D),('mi_5',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',C),('silence',D),('do_3',D),('mi_3',D),('la_3',D),('si_3',C),('silence',D),('mi_3',D),('sol#_3',D),('si_3',D),('do_4',C),('silence',D),('mi_3',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',C),('silence',D),('do_3',D),('mi_3',D),('la_3',D),('si_3',C),('silence',D),('mi_3',D),('do_4',D),('si_3',D),('la_3',C),('silence',D),('do_4',D),('do_4',D),('do_4',D),('do_4',N),('fa_4',Dpt),('mi_4',T),('mi_4',C),('re_4',C),('la#_4',Dpt),('la_4',T),('la_4',D),('sol_4',D),('fa_4',D),('mi_4',D),('re_4',D),('do_4',D),('la#_3',C),('la_3',C),('la_3',T),('sol_3',T),('la_3',T),('si_3',T),('do_4',N),('re_4',D),('re#_4',D),('mi_4',Cpt),('mi_4',D),('fa_4',D),('la_3',D),('do_4',N),('re_4',Dpt),('si_3',T),('do_4',T),('sol_4',T),('sol_3',T),('sol_4',T),('la_3',T),('sol_4',T),('si_3',T),('sol_4',T),('do_4',T),('sol_4',T),('re_4',T),('sol_4',T),('mi_4',T),('sol_4',T),('do_5',T),('si_4',T),('la_4',T),('sol_4',T),('fa_4',T),('mi_4',T),('re_4',T),('sol_4',T),('fa_4',T),('re_4',T),('do_4',T),('sol_4',T),('sol_3',T),('sol_4',T),('la_3',T),('sol_4',T),('si_3',T),('sol_4',T),('do_4',T),('sol_4',T),('re_4',T),('sol_4',T),('mi_4',T),('sol_4',T),('do_5',T),('si_4',T),('la_4',T),('sol_4',T),('fa_4',T),('mi_4',T),('re_4',T),('sol_4',T),('fa_4',T),('re_4',T),('mi_4',T),('fa_4',T),('mi_4',T),('re#_4',T),('mi_4',T),('si_3',T),('mi_4',T),('re#_4',T),('mi_4',T),('si_3',T),('mi_4',T),('re#_4',T),('mi_4',Cpt),('si_3',D),('mi_4',D),('re#_4',D),('mi_4',Cpt),('si_3',D),('mi_4',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',C),('silence',D),('do_3',D),('mi_3',D),('la_3',D),('si_3',C),('silence',D),('mi_3',D),('sol#_3',D),('si_3',D),('do_4',C),('silence',D),('mi_3',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',C),('silence',D),('do_3',D),('mi_3',D),('la_3',D),('si_3',C),('silence',D),('mi_3',D),('do_4',D),('si_3',D),('la_3',C),('silence',D),('si_3',D),('do_4',D),('re_4',D),('mi_4',Cpt),('sol_3',D),('fa_4',D),('mi_4',D),('re_4',Cpt),('fa_3',D),('mi_4',D),('re_4',D),('do_4',Cpt),('mi_3',D),('re_4',D),('do_4',D),('si_3',C),('silence',D),('mi_3',D),('mi_4',D),('silence',D),('silence',D),('mi_4',D),('mi_5',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('re_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',C),('silence',D),('do_3',D),('mi_3',D),('la_3',D),('si_3',C),('silence',D),('mi_3',D),('sol#_3',D),('si_3',D),('do_4',C),('silence',D),('mi_3',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',C),('silence',D),('do_3',D),('mi_3',D),('la_3',D),('si_3',C),('silence',D),('mi_3',D),('do_4',D),('si_3',D),('la_3',C),('silence',D),('silence',D),('silence',C),('do#_4',Npt),('re_4',N),('mi_4',D),('fa_4',D),('fa_4',N),('fa_4',C),('mi_4',Npt),('re_4',N),('do_4',D),('si_3',D),('la_3',N),('la_3',C),('la_3',C),('do_4',C),('si_3',C),('la_3',Npt),('do#_4',Npt),('re_4',N),('mi_4',D),('fa_4',D),('fa_4',N),('fa_4',C),('fa_4',Npt),('re#_4',N),('re_4',D),('do_4',D),('la#_3',N),('la_3',C),('sol#_3',N),('sol_3',C),('la_3',Npt),('si_3',N),('silence',C),('la_2',Tpt),('do_3',Tpt),('mi_3',Tpt),('la_3',Tpt),('do_4',Tpt),('mi_4',Tpt),('re_4',Tpt),('do_4',Tpt),('si_3',Tpt),('la_3',Tpt),('do_4',Tpt),('mi_4',Tpt),('la_4',Tpt),('do_5',Tpt),('mi_5',Tpt),('re_5',Tpt),('do_5',Tpt),('si_4',Tpt),('la_3',Tpt),('do_4',Tpt),('mi_4',Tpt),('la_4',Tpt),('do_5',Tpt),('mi_5',Tpt),('re_5',Tpt),('do_5',Tpt),('si_4',Tpt),('la#_4',Tpt),('la_4',Tpt),('sol#_4',Tpt),('sol_4',Tpt),('fa#_4',Tpt),('fa_4',Tpt),('mi_4',Tpt),('re#_4',Tpt),('re_4',Tpt),('do#_4',Tpt),('do_4',Tpt),('si_3',Tpt),('la#_3',Tpt),('la_3',Tpt),('sol#_3',Tpt),('sol_3',Tpt),('fa#_3',Tpt),('fa_3',Tpt),('mi_3',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',Cpt),('do_3',D),('mi_3',D),('la_3',D),('si_3',Cpt),('mi_3',D),('sol#_3',D),('si_3',D),('do_4',C),('silence',D),('mi_3',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',Cpt),('do_3',D),('mi_3',D),('la_3',D),('si_3',Cpt),('mi_3',D),('do_4',D),('si_3',D),('la_3',Cpt),('silence',Cpt),('silence',Cpt),('sol_3',D),('fa_4',D),('mi_4',D),('re_4',N),('silence',C),('silence',Cpt),('mi_3',D),('re_4',D),('do_4',D),('si_3',Cpt),('mi_3',D),('mi_4',C),('mi_4',C),('mi_5',Cpt),('re#_4',D),('mi_4',D),('silence',D),('silence',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',Cpt),('do_3',D),('mi_3',D),('la_3',D),('si_3',Cpt),('mi_3',D),('sol#_3',D),('si_3',D),('do_4',C),('silence',D),('mi_3',D),('mi_4',D),('re#_4',D),('mi_4',D),('re#_4',D),('mi_4',D),('si_3',D),('re_4',D),('do_4',D),('la_3',Cpt),('do_3',D),('mi_3',D),('la_3',D),('si_3',Cpt),('mi_3',D),('do_4',D),('si_3',D),('la_3',Npt),] }
La_panthere_rose = {'titre':'Pink Panther theme', 'tempo':120,
    'notes':[ ('silence',B),('silence',N),('silence',C),('re#_3',C),('mi_3',Npt),('silence',C),('fa#_3',C),('sol_3',Npt),('silence',C),('re#_3',C),('mi_3',Cpt),('fa#_3',C),('sol_3',Cpt),('do_4',C),('si_3',Cpt),('mi_3',C),('sol_3',Cpt),('si_3',C),('la#_3',B),('la_3',Dpt),('sol_3',Dpt),('mi_3',Dpt),('re_3',Dpt),('mi_3',B),('silence',N),('silence',C),('re#_3',N),('mi_3',Npt),('silence',C),('fa#_3',C),('sol_3',Npt),('silence',C),('re#_3',C),('mi_3',Cpt),('fa#_3',C),('sol_3',Cpt),('do_4',C),('si_3',Cpt),('sol_3',C),('si_3',Cpt),('mi_4',C),('re#_4',R),('re_4',B),('silence',N),('silence',C),('re#_3',C),('mi_3',Npt),('silence',C),('fa#_3',C),('sol_3',Npt),('silence',C),('re#_3',C),('mi_3',Cpt),('fa#_3',C),('sol_3',Cpt),('do_4',C),('si_3',Cpt),('mi_3',C),('sol_3',Cpt),('si_3',C),('la#_3',B),('la_3',Dpt),('sol_3',Dpt),('mi_3',Dpt),('re_3',Dpt),('mi_3',Npt),('silence',N),('silence',N),('mi_4',Cpt),('re_4',C),('si_3',Cpt),('la_3',C),('sol_3',Cpt),('mi_3',Cpt),('la#_3',D),('la_3',Cpt),('la#_3',D),('la_3',Cpt),('la#_3',D),('la_3',Cpt),('la#_3',D),('la_3',Cpt),('sol_3',Dpt),('mi_3',Dpt),('re_3',Dpt),('mi_3',D),('mi_3',D),('mi_3',B),] }
Harry_Potter = {'titre':'Hedwig\'s theme (Harry Potter)', 'tempo':144,
    'notes':[ ('silence',B),('re_3',N),('sol_3',Npt),('la#_3',C),('la_3',N),('sol_3',B),('re_4',N),('do_4',Bpt),('la_3',Bpt),('sol_3',Npt),('la#_3',C),('la_3',N),('fa_3',B),('sol#_3',N),('re_3',Rpt),('re_3',N),('sol_3',Npt),('la#_3',C),('la_3',N),('sol_3',B),('re_4',N),('fa_4',B),('mi_4',N),('re#_4',B),('si_3',N),('re#_4',Npt),('re_4',C),('do#_4',N),('do#_3',B),('si_3',N),('sol_3',Rpt),('la#_3',N),('re_4',B),('la#_3',N),('re_4',B),('la#_3',N),('re#_4',B),('re_4',N),('do#_4',B),('la_3',N),('la#_3',Npt),('re_4',C),('do#_4',N),('do#_3',B),('re_3',N),('re_4',Rpt),('silence',N),('la#_3',N),('re_4',B),('la#_3',N),('re_4',B),('la#_3',N),('fa_4',B),('mi_4',N),('re#_4',B),('si_3',N),('re#_4',Npt),('re_4',C),('do#_4',N),('do#_3',B),('la#_3',N),('sol_3',Rpt),] }
Keyboard_cat = {'titre':'Keyboard cat', 'tempo':160,
    'notes':[ ('silence',R),('silence',R),('do_3',N),('mi_3',N),('sol_3',N),('mi_3',N),('do_3',N),('mi_3',C),('sol_3',Npt),('mi_3',N),('la_2',N),('do_3',N),('mi_3',N),('do_3',N),('la_2',N),('do_3',C),('mi_3',Npt),('do_3',N),('sol_2',N),('si_2',N),('re_3',N),('si_2',N),('sol_2',N),('si_2',C),('re_3',Npt),('si_2',N),('sol_2',N),('sol_2',C),('sol_2',Npt),('sol_2',C),('sol_2',N),('sol_2',N),('sol_2',N),('sol_2',C),('sol_2',N),('do_3',N),('mi_3',N),('sol_3',N),('mi_3',N),('do_3',N),('mi_3',C),('sol_3',Npt),('mi_3',N),('la_2',N),('do_3',N),('mi_3',N),('do_3',N),('la_2',N),('do_3',C),('mi_3',Npt),('do_3',N),('sol_2',N),('si_2',N),('re_3',N),('si_2',N),('sol_2',N),('si_2',C),('re_3',Npt),('si_2',N),('sol_2',Rpt),] }
Game_of_Thrones = {'titre':'Game of Thrones', 'tempo':85,
    'notes':[ ('sol_3',C),('do_3',C),('re#_3',D),('fa_3',D),('sol_3',C),('do_3',C),('re#_3',D),('fa_3',D),('sol_3',C),('do_3',C),('re#_3',D),('fa_3',D),('sol_3',C),('do_3',C),('re#_3',D),('fa_3',D),('sol_3',C),('do_3',C),('mi_3',D),('fa_3',D),('sol_3',C),('do_3',C),('mi_3',D),('fa_3',D),('sol_3',C),('do_3',C),('mi_3',D),('fa_3',D),('sol_3',C),('do_3',C),('mi_3',D),('fa_3',D),('sol_3',Npt),('do_3',Npt),('re#_3',D),('fa_3',D),('sol_3',N),('do_3',N),('re#_3',D),('fa_3',D),('re_3',Rpt),('fa_3',Npt),('la#_2',Npt),('re#_3',D),('re_3',D),('fa_3',N),('la#_2',Npt),('re#_3',D),('re_3',D),('do_3',Rpt),('sol_3',Npt),('do_3',Npt),('re#_3',D),('fa_3',D),('sol_3',N),('do_3',N),('re#_3',D),('fa_3',D),('re_3',Rpt),('fa_3',Npt),('la#_2',Npt),('re#_3',D),('re_3',D),('fa_3',N),('la#_2',Npt),('re#_3',D),('re_3',D),('do_3',Rpt),('sol_3',Npt),('do_3',Npt),('re#_3',D),('fa_3',D),('sol_3',N),('do_3',N),('re#_3',D),('fa_3',D),('re_3',Bpt),('fa_3',Npt),('la#_2',Npt),('re_3',Cpt),('re#_3',Cpt),('re_3',Cpt),('la#_2',Cpt),('do_3',Rpt),('do_4',Bpt),('la#_3',Bpt),('do_3',Bpt),('sol_3',Bpt),('re#_3',Bpt),('re#_3',Npt),('fa_3',Npt),('sol_3',Rpt),('do_4',Bpt),('la#_3',Bpt),('do_3',Bpt),('sol_3',Bpt),('re#_3',Bpt),('re#_3',Npt),('re_3',Npt),('do_4',C),('sol_3',C),('sol#_3',D),('la#_3',D),('do_4',C),('sol_3',C),('sol#_3',D),('la#_3',D),('do_4',C),('sol_3',C),('sol#_3',D),('la#_3',D),('do_4',C),('sol_3',C),('sol#_3',D),('la#_3',D),('silence',N),('sol#_4',D),('la#_4',D),('do_5',C),('sol_4',C),('sol#_4',D),('la#_4',D),('do_5',C),('sol_4',D),('sol#_4',D),('la#_4',D),('do_5',C),('sol_4',C),('sol#_4',D),('la#_4',D),] }
Greensleeves = {'titre':'Greensleeves', 'tempo':70,
    'notes':[ ('sol_3',C),('la#_3',N),('do_4',C),('re_4',Cpt),('re#_4',D),('re_4',C),('do_4',N),('la_3',C),('fa_3',Cpt),('sol_3',D),('la_3',C),('la#_3',N),('sol_3',C),('sol_3',Cpt),('fa#_3',D),('sol_3',C),('la_3',N),('fa#_3',C),('re_3',N),('sol_3',C),('la#_3',N),('do_4',C),('re_4',Cpt),('re#_4',D),('re_4',C),('do_4',N),('la_3',C),('fa_3',Cpt),('sol_3',D),('la_3',C),('la#_3',Cpt),('la_3',D),('sol_3',C),('fa#_3',Cpt),('mi_3',D),('fa#_3',C),('sol_3',Bpt),('fa_4',B),('mi_4',D),('re_4',C),('do_4',N),('la_3',C),('fa_3',Cpt),('sol_3',D),('la_3',C),('la#_3',N),('sol_3',C),('sol_3',Cpt),('fa#_3',D),('sol_3',C),('la_3',N),('fa#_3',C),('re_3',N),('fa_4',B),('mi_4',D),('re_4',C),('do_4',N),('la_3',C),('fa_3',Cpt),('sol_3',D),('la_3',C),('la#_3',Cpt),('la_3',D),('sol_3',C),('fa#_3',Cpt),('mi_3',D),('fa#_3',C),('sol_3',Bpt),('sol_3',C),('la#_3',N),('do_4',C),('re_4',Cpt),('re#_4',D),('re_4',C),('do_4',N),('la_3',C),('fa_3',Cpt),('sol_3',D),('la_3',C),('la#_3',N),('sol_3',C),('sol_3',Cpt),('fa#_3',D),('sol_3',C),('la_3',N),('fa#_3',C),('re_3',N),('sol_3',C),('la#_3',N),('do_4',C),('re_4',Cpt),('re#_4',D),('re_4',C),('do_4',N),('la_3',C),('fa_3',Cpt),('sol_3',D),('la_3',C),('la#_3',Cpt),('la_3',D),('sol_3',C),('fa#_3',Cpt),('mi_3',D),('fa#_3',C),('sol_3',Bpt),('fa_4',B),('mi_4',D),('re_4',C),('do_4',N),('la_3',C),('fa_3',Cpt),('sol_3',D),('la_3',C),('la#_3',N),('sol_3',C),('sol_3',Cpt),('fa#_3',D),('sol_3',C),('la_3',N),('fa#_3',C),('re_3',N),('fa_4',B),('mi_4',D),('re_4',C),('do_4',N),('la_3',C),('fa_3',Cpt),('sol_3',D),('la_3',C),('la#_3',Cpt),('la_3',D),('sol_3',C),('fa#_3',Cpt),('mi_3',D),('fa#_3',C),('sol_3',Bpt),] }
Baby_Elephant_Walk = {'titre':'Baby Elephant Walk', 'tempo':132,
    'notes':[ ('do_3',Cpt),('mi_3',D),('sol_3',C),('do_4',C),('mi_4',C),('re_4',C),('do_4',C),('la_3',C),('fa#_3',C),('sol_3',C),('silence',N),('silence',B),('do_3',Cpt),('mi_3',D),('sol_3',C),('do_4',C),('mi_4',C),('re_4',C),('do_4',C),('la_3',C),('sol_3',Bpt),('la_3',C),('re#_3',R),('la_3',C),('mi_3',C),('do_3',C),('silence',N),('silence',B),('do_3',Cpt),('mi_3',D),('sol_3',C),('do_4',C),('mi_4',C),('re_4',C),('do_4',C),('la_3',C),('fa#_3',C),('sol_3',C),('silence',N),('silence',N),('silence',C),('sol_3',C),('re_4',N),('re_4',N),('si_3',C),('sol_3',C),('silence',C),('sol_3',C),('do_4',N),('do_4',N),('la#_3',D),('do_4',D),('la#_3',D),('sol_3',D),('fa_3',C),('re#_3',C),('fa#_3',N),('fa#_3',N),('fa_3',D),('sol_3',D),('fa_3',D),('re#_3',D),('do_3',C),('sol_3',C),('la#_3',C),('do_4',C),('silence',N),('silence',B),] }
Take_on_me_Aha = {'titre':'Take on me - A-ha', 'tempo':140,
    'notes':[ ('fa#_4',C),('fa#_4',C),('re_4',C),('si_3',C),('silence',C),('si_3',C),('silence',C),('mi_4',C),('silence',C),('mi_4',C),('silence',C),('mi_4',C),('sol#_4',C),('sol#_4',C),('la_4',C),('si_4',C),('la_4',C),('la_4',C),('la_4',C),('mi_4',C),('silence',C),('re_4',C),('silence',C),('fa#_4',C),('silence',C),('fa#_4',C),('silence',C),('fa#_4',C),('mi_4',C),('mi_4',C),('fa#_4',C),('mi_4',C),('fa#_4',C),('fa#_4',C),('re_4',C),('si_3',C),('silence',C),('si_3',C),('silence',C),('mi_4',C),('silence',C),('mi_4',C),('silence',C),('mi_4',C),('sol#_4',C),('sol#_4',C),('la_4',C),('si_4',C),('la_4',C),('la_4',C),('la_4',C),('mi_4',C),('silence',C),('re_4',C),('silence',C),('fa#_4',C),('silence',C),('fa#_4',C),('silence',C),('fa#_4',C),('mi_4',C),('mi_4',C),('fa#_4',C),('mi_4',C),('fa#_4',C),('fa#_4',C),('re_4',C),('si_3',C),('silence',C),('si_3',C),('silence',C),('mi_4',C),('silence',C),('mi_4',C),('silence',C),('mi_4',C),('sol#_4',C),('sol#_4',C),('la_4',C),('si_4',C),('la_4',C),('la_4',C),('la_4',C),('mi_4',C),('silence',C),('re_4',C),('silence',C),('fa#_4',C),('silence',C),('fa#_4',C),('silence',C),('fa#_4',C),('mi_4',C),('mi_4',C),('fa#_4',C),('mi_4',C),] }
Le_Parrain_theme = {'titre':'The Godfather theme', 'tempo':80,
    'notes':[ ('silence',N),('silence',C),('silence',C),('silence',C),('mi_3',C),('la_3',C),('do_4',C),('si_3',C),('la_3',C),('do_4',C),('la_3',C),('si_3',C),('la_3',C),('fa_3',C),('sol_3',C),('mi_3',B),('mi_3',C),('la_3',C),('do_4',C),('si_3',C),('la_3',C),('do_4',C),('la_3',C),('do_4',C),('la_3',C),('mi_3',C),('re#_3',C),('re_3',B),('re_3',C),('fa_3',C),('sol#_3',C),('si_3',B),('re_3',C),('fa_3',C),('sol#_3',C),('la_3',B),('do_3',C),('do_3',C),('sol_3',C),('fa_3',C),('mi_3',C),('sol_3',C),('fa_3',C),('fa_3',C),('mi_3',C),('mi_3',C),('sol#_3',C),('la_3',B),('silence',C),('la_3',C),('la_3',C),('sol#_3',C),('sol_3',B),('si_3',C),('la_3',C),('fa_3',C),('mi_3',B),('mi_3',C),('sol_3',C),('mi_3',C),('re_3',B),('re_3',C),('re_3',C),('fa_3',C),('re#_3',C),('mi_3',B),('silence',C),('mi_3',C),('la_3',C),('do_4',C),('si_3',C),('la_3',C),('do_4',C),('la_3',C),('si_3',C),('la_3',C),('fa_3',C),('sol_3',C),('mi_3',B),('mi_3',C),('la_3',C),('do_4',C),('si_3',C),('la_3',C),('do_4',C),('la_3',C),('do_4',C),('la_3',C),('mi_3',C),('re#_3',C),('re_3',B),('re_3',C),('fa_3',C),('sol#_3',C),('si_3',B),('re_3',C),('fa_3',C),('sol#_3',C),('la_3',B),('do_3',C),('do_3',C),('sol_3',C),('fa_3',C),('mi_3',C),('sol_3',C),('fa_3',C),('fa_3',C),('mi_3',C),('mi_3',C),('sol#_3',C),('la_3',B),('silence',C),('la_3',C),('la_3',C),('sol#_3',C),('sol_3',B),('si_3',C),('la_3',C),('fa_3',C),('mi_3',B),('mi_3',C),('sol_3',C),('mi_3',C),('re_3',B),('re_3',C),('re_3',C),('fa_3',C),('re#_3',C),('mi_3',B),] }

#TODO : faire la mélodie du flic de beverly hills + le lion est mort ce soir

melodies = [
     jingle,
     Star_Trek_intro,
     Silent_Night,
     We_Wish_You_a_Merry_Christmas,
     Happy_Birthday,
     Pacman,
     Theme_A_from_Tetris_Korobeiniki,
     Super_Mario_Bros_theme_by_Koji_Kondo,
     The_Legend_of_Zelda_theme,
     At_Dooms_Gate_E1M1,
     Vampire_Killer_Castlevania,
     Star_Wars_theme,
     Dart_Vader_theme,
     Nokia_Ringtone,
     Badinerie_Johann_Sebastian_Bach,
     La_lettre_a_Elise_Beethoven,
     La_panthere_rose,
     Harry_Potter,
     Keyboard_cat,
     Game_of_Thrones,
     Greensleeves,
     Baby_Elephant_Walk,
     Take_on_me_Aha,
     Le_Parrain_theme,
]

# Si on veut jouer seulement 1 mélodie, décommenter cette ligne :
joue_melodie(jingle)

idx_melodie = -1
print(f"attend l'appui sur le bouton Pin{pinButton}")
while True:

    if button.value()==0: # bouton enfoncé...
        while button.value()==0: # ...on attend qu'il soit relevé
            sleep(0.1)
        idx_melodie+=1 # prochaine chanson
        idx_melodie%=len(melodies) # si on arrive à la dernière, on reboucle à la 1ère chanson
    
        melodie=melodies[idx_melodie]
        joue_melodie(melodie)
    sleep(0.1)

