# Imports
from machine import ADC
import time

# Configuration
ADC_NB = 0

# Declaration
potar = ADC(ADC_NB)

# Variables

# Fonction qui lit le potentiometre
def lit_potar():
    global potar
    return potar.read_u16()

# Message d'information
print("Example ADC Potentiometre....")

valeur_precedente = lit_potar()

# Boucle principale
while True:
    # on effectue la boucle toutes les 0.3 ms
    time.sleep(0.3)
    # lit la valeur du potentiometre
    valeur_courante  = lit_potar()
    # test si la valeur lue est différente de la précédente
    if valeur_courante != valeur_precedente:
        # affiche la valeur du potentiometre
        print("La valeur est")
        print(valeur_courante)
        # sauvegarde la nouvelle valeur du potentiometre
        valeur_precedente = valeur_courante
        
    