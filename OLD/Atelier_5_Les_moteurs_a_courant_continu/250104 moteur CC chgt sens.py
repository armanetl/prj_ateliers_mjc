from machine import Pin, PWM
from time import sleep

in1= Pin(16, Pin.OUT, Pin.PULL_UP)
in2= Pin(17, Pin.OUT, Pin.PULL_UP)

pwm = PWM(Pin(15))
pwm.freq(1000)
duty=0
pwm.duty_u16(duty)


#min_duty = 10000
#max_duty = 30000

duty = 16000
print(duty)
in1.value(0)
in2.value(1)
pwm.duty_u16(duty)
sleep(5)

duty=0
in1.value(1)
in2.value(1)
print("changement de sens")
sleep(3)

duty=16000
in1.value(1)
in2.value(0)
pwm.duty_u16(duty)
sleep(5)

duty=0
in1.value(1)
in2.value(1)
pwm.deinit()
