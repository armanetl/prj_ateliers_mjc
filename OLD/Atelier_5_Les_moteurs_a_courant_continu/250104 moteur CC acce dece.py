from machine import Pin, PWM
from time import sleep

in1= Pin(16, Pin.OUT, Pin.PULL_UP)
in2= Pin(17, Pin.OUT, Pin.PULL_UP)

pwm = PWM(Pin(15))
pwm.freq(1000)
duty = 0
pwm.duty_u16(duty)
sleep(0.1)

min_duty = 10000
max_duty = 30000



for duty in range(min_duty, max_duty, 500):
    print(duty)
    in1.value(0)
    in2.value(1)
    pwm.duty_u16(duty)
    sleep(0.7)

for duty in range(max_duty, min_duty, -500):
    print(duty)
    in1.value(0)
    in2.value(1)
    pwm.duty_u16(duty)
    sleep(0.7)
duty=0
in1.value(1)
in2.value(1)
pwm.deinit()
