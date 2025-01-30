from machine import Pin, PWM
from time import sleep

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



for duty in range(min_duty,max_duty,500):
    print(duty)
    in1.value(0)
    in2.value(1)
    pwm.duty_u16(duty)
    sleep(1)

for duty in range(max_duty,min_duty,-500):
    print(duty)
    in1.value(0)
    in2.value(1)
    pwm.duty_u16(duty)
    sleep(1)
    
in1.value(1)
in2.value(1)
pwm.deinit()

  

