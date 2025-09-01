from machine import Pin

BP = Pin(15, Pin.IN, Pin.PULL_UP)

LED = Pin(0, Pin.OUT)

LED.value(0) # on eteint le lampe

# defintion des etats
STATE_L1_OFF = 0
STATE_L2_ON = 1
STATE_L3_ON = 2
STATE_L4_OFF = 3

# variable memorisant l'etat courant
current_state = STATE_L1_OFF


# boucle principale
while True:
    # lit la valeur du bp
    bp_value = BP.value()
    # en fonction de l'etat ou l'on se trouve
    if current_state == STATE_L1_OFF:
        # on regarde l'etat du bouton
        # si il est a 1 on effectue l'action
        if bp_value == 0:
            print(f"bp {BP.value()}, state {current_state}")
            # on allume la led et on change d'etat
            LED.value(1)
            current_state = STATE_L2_ON
            
    elif current_state == STATE_L2_ON:
        if bp_value == 1:
            print(f"bp {BP.value()}, state {current_state}")
            # on change d'etat sans modifier la led
            current_state = STATE_L3_ON
            
    elif current_state == STATE_L3_ON:
        if bp_value == 0:
            print(f"bp {BP.value()}, state {current_state}")
            # on change d'etat et on eteint le led
            LED.value(0)
            current_state = STATE_L4_OFF
            
    elif current_state == STATE_L4_OFF:
        if bp_value == 1:
            print(f"bp {BP.value()}, state {current_state}")
            # on change d'etat sans modifier la led
            current_state = STATE_L1_OFF
            print(f"bp {BP.value()}, state {current_state}")
            
# fin

        