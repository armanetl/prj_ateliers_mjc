from machine import Pin, PWM
from rotary_irq_rp2 import RotaryIRQ
import time

in1 = Pin(16,Pin.OUT,Pin.PULL_DOWN)
in2 = Pin(17,Pin.OUT,Pin.PULL_DOWN)

pwm = PWM(Pin(15))
pwm.freq(1000)
pwm.duty_u16(0)

min_duty= 18000
max_duty= 22000#30000

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
        else:
            duty =  int(min_duty + val_new * increment)
            in1.value(0)
            in2.value(1)
            pwm.duty_u16(duty)
    time.sleep_ms(50)


