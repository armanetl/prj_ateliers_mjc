from machine import Pin, PWM
from rotary_irq_rp2 import RotaryIRQ
import time

# declaration de l'encoder
r = RotaryIRQ(pin_num_clk=13,pin_num_dt=12,reverse=False,
              incr=1,range_mode=RotaryIRQ.RANGE_UNBOUNDED,
              pull_up=True,half_step=False)

val_old = r.value()

while True:
    val_new = r.value()
    if val_old != val_new:
        # on affiche la valeur de l'encoder        
        print("step =", val_new)
        val_old = val_new     
    time.sleep_ms(50)

  

