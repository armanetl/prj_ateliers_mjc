from machine import Pin
import time
import utime

button_do = Pin(6, Pin.IN, Pin.PULL_UP)
button_re = Pin(7, Pin.IN, Pin.PULL_UP)
button_mi = Pin(8, Pin.IN, Pin.PULL_UP)
button_fa = Pin(9, Pin.IN, Pin.PULL_UP)

do_last = time.ticks_ms()
re_last = time.ticks_ms()
mi_last = time.ticks_ms()
fa_last = time.ticks_ms()

def button_handler(pin):
        global do_last, re_last, mi_last, fa_last
        global button_do, button_re, button_mi, button_fa
      
        if pin is button_do:
            if time.ticks_diff(time.ticks_ms(), do_last) > 500:
                print('DO')
                do_last = time.ticks_ms()
        elif pin is button_re:
            if time.ticks_diff(time.ticks_ms(), re_last) > 500:
                print('RE')
                re_last = time.ticks_ms()
        elif pin is button_mi:
            if time.ticks_diff(time.ticks_ms(), mi_last) > 500:
                print('MI')
                mi_last = time.ticks_ms()
        elif pin is button_fa:
            if time.ticks_diff(time.ticks_ms(), fa_last) > 500:
                print('FA')
                fa_last = time.ticks_ms()
                
button_do.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_re.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_mi.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_fa.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
     