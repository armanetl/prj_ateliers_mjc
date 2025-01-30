from machine import Pin, PWM
from rotary_irq_rp2 import RotaryIRQ
from neopixel import Neopixel
import time

# declaration du ruban de leds (Pin 0)
NUM_LED = 8
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)
couleur_noir = (0,0,0)
couleurs = [couleur_vert,(0,200,0),(0,150,0),(50,100,0),(100,50,0),(150,0,0),(200,0,0),couleur_rouge]
leds.brightness(15)
leds.clear()
leds.show()

'''
# Moteur 1 : Voiture téléguidée
in1 = Pin(16,Pin.OUT,Pin.PULL_DOWN)
in2 = Pin(17,Pin.OUT,Pin.PULL_DOWN)
pwm = PWM(Pin(15))
min_duty= 18000
max_duty= 22000#30000

'''
# Moteur 2 : Moteur achat
in1 = Pin(20,Pin.OUT,Pin.PULL_DOWN)
in2 = Pin(19,Pin.OUT,Pin.PULL_DOWN)
pwm = PWM(Pin(18))
min_duty= 12000
max_duty= 20000#30000

# On stoppe le moteur
pwm.freq(1000)
pwm.duty_u16(0)
in1.value(1)
in2.value(1)

# declaration de l'encoder
r = RotaryIRQ(pin_num_clk=13,pin_num_dt=12,reverse=False,
              incr=1,range_mode=RotaryIRQ.RANGE_UNBOUNDED,
              pull_up=True,half_step=False)

val_old = r.value()

increment = (max_duty - min_duty)/10

while True:
    val_new = r.value()
    if val_old != val_new:
        # on affiche la valeur de l'encoder        
        print("step =", val_new)
        val_old = val_new
        if (val_new == 0) or (val_new < 0):
            in1.value(1)
            in2.value(1)
            leds.set_pixel(0,couleurs[0])
            leds.show()
        else:
            leds.clear()
            leds.show()
            #leds.set_pixel_line_gradient(0,val_new,couleur_vert,couleur_rouge)
            for i in range (0,val_new):
                leds.set_pixel(i,couleurs[i])
            leds.show()
            duty =  int(min_duty + val_new * increment)
            in1.value(0)
            in2.value(1)
            pwm.duty_u16(duty)
    time.sleep_ms(50)


