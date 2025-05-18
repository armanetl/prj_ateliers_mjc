from machine import Pin, PWM
from time import sleep

in1 = Pin(16,Pin.OUT,Pin.PULL_DOWN)
in2 = Pin(17,Pin.OUT,Pin.PULL_DOWN)

pwm = PWM(Pin(15))
pwm.freq(1000)
pwm.duty_u16(0)


in1.value(0)
in2.value(1)
pwm.duty_u16(25000)
sleep(5)

in1.value(1)
in2.value(1)
pwm.duty_u16(0)
sleep(3)

in1.value(1)
in2.value(0)
pwm.duty_u16(25000)
sleep(5)
    
in1.value(1)
in2.value(1)
pwm.duty_u16(0)
pwm.deinit()

  

