from machine import Pin, PWM
from time import sleep

in1 = Pin(16,Pin.OUT,Pin.PULL_DOWN)
in2 = Pin(17,Pin.OUT,Pin.PULL_DOWN)

pwm = PWM(Pin(15))
pwm.freq(1000)
pwm.duty_u16(0)

min_duty= 18000
max_duty= 22000#30000

for duty in range(min_duty,max_duty,500):
    print(duty)
    in1.value(0)
    in2.value(1)
    pwm.duty_u16(duty)
    sleep(0.5)

for duty in range(max_duty,min_duty,-500):
    print(duty)
    in1.value(0)
    in2.value(1)
    pwm.duty_u16(duty)
    sleep(0.5)
    
in1.value(1)
in2.value(1)
pwm.deinit()

  

