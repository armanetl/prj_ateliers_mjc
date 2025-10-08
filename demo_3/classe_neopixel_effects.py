from machine import Pin
from time import sleep, time
from neopixel import Neopixel

class NeoPixelEffects:
    def __init__(self, pin_num, num_leds):
        self.num_leds = num_leds
        self.np = Neopixel(num_leds, 0, pin_num, "GRB")
        self.np.brightness(180)
        # --- Palette de couleurs froides ---
        self.palette_froid = [
            (0, 0, 30),     # bleu foncé
            (0, 0, 80),     # bleu moyen
            (0, 40, 120),   # bleu clair
            (80, 150, 255), # bleu glacier
            (180, 220, 255) # blanc bleuté
        ]
        # --- Palette de couleurs chaudes ---
        self.palette_chaud = [
            (60, 0, 0),      # rouge sombre
            (120, 10, 0),    # rouge vif
            (180, 40, 0),    # rouge orangé
            (255, 100, 0),   # orange chaud
            (255, 180, 50),  # jaune doré
            (255, 220, 100)  # jaune clair (lueur de flamme)
        ]
        # --- Palette de couleurs de Noel ---
        self.palette_noel = [
            (255, 0, 0),     # rouge vif
            (0, 255, 0),     # vert vif
            (255, 200, 0),   # jaune chaud (optionnel)
            (0, 128, 0),     # vert sapin
            (200, 0, 0)      # rouge foncé
        ]
        # --- Palette de couleurs d'une plante heureuse ---
        self.palette_plante_ok = [
            (0, 128, 0),    # vert sapin
            (0, 200, 0),    # vert vif
            (50, 255, 50),  # vert tendre lumineux
            (100, 255, 100),# vert clair
            (150, 255, 150) # vert très lumineux
        ]
        
    def set_all(self, color):
        for i in range(self.num_leds):
            self.np[i] = color
        self.np.show()
    
    def blink(self, color, times=3, delay=0.2):
        for _ in range(times):
            self.set_all(color)
            sleep(delay)
            self.set_all((0,0,0))
            sleep(delay)

    def animation_palette(self, palette, vitesse=0.1, duree=5):
        """
        Fait défiler les couleurs d'une palette sur le ruban pendant 'duree' secondes.

        :param palette: liste de tuples (R,G,B) ou (R,G,B,W)
        :param vitesse: temps entre chaque décalage (secondes)
        :param duree: durée totale de l'animation (secondes)
        """
        debut = time()
        while time() - debut < duree:
            for color in palette:
                self.np.rotate_right()
                self.np[0] = color
                self.np.show()
                sleep(vitesse)
        # Éteindre le ruban à la fin
        self.np.clear()
        self.np.show()

    
if __name__ == '__main__':
    neo = NeoPixelEffects(0, 24)
    print("Guirlande rouge")
    neo.blink((255, 0, 0)) #Rouge
    print("Animation chaud 🔥")
    neo.animation_palette(neo.palette_chaud,0.1,5)
    print("Animation froid ❄")
    neo.animation_palette(neo.palette_froid,0.1,5)
    print("Animation Noel 🎅")
    neo.animation_palette(neo.palette_noel,0.1,5)
    print("Animation Plante OK 🌱")
    neo.animation_palette(neo.palette_plante_ok,0.1,5)
