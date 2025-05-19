from classe_music_P import Music_P
import time

#r2d2_name = "PicoGo"
r2d2_name = "Yaboom"
#r2d2_name = "Titan"

if (r2d2_name == "PicoGo"):
    from robot_picogo import RobotPicoGo
    r2d2 = RobotPicoGo()
elif (r2d2_name == "Yaboom"):
    from robot_yaboom import RobotYaboom
    r2d2 = RobotYaboom()
elif (r2d2_name == "Titan"):
    from robot_titan import RobotTitan
    r2d2 = RobotTitan()
    
def main_exemple_buzzer():

    global r2d2
    
    # Declaration de la classe music
    music = Music_P(r2d2.buzzer)
    
    #melodie = music.Silent_Night
    #melodie = music.We_Wish_You_a_Merry_Christmas
    #melodie = music.Pacman
    melodie = music.Theme_A_from_Tetris_Korobeiniki
    #melodie = music.Super_Mario_Bros_theme_by_Koji_Kondo
    #melodie = music.The_Legend_of_Zelda_theme
    #melodie = music.Star_Wars_theme
    #melodie = music.Dart_Vader_theme
    #melodie = music.Nokia_Ringtone
    #melodie = music.self.La_lettre_a_Elise_Beethoven
    #melodie = music.self.Take_on_me_Aha
   
    try:
        while True:
            music.joue_melodie(melodie)
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')

if __name__ == '__main__':
    main_exemple_buzzer()