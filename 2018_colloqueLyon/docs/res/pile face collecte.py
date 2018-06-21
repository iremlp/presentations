# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
# code utilisé pour l'atelier colloque C2i collège
# auteur : groupe InEFLP IREM de Marseille

from microbit import *
import random
import radio

def anim():
    tab = [Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW]
    for i in tab:
        display.show(i)
        sleep(50)

def lancer(n, p):
    anim()
    n += 1
    tirage = random.randint(0, 99)
    if tirage <= 55:
        display.show("P")
        p += 1
        radio.send('1')
    else:
        display.show("F")
        radio.send('0')
    sleep(2)
    return (n, p)


radio.on()

p = 0
n = 0
f = 0

# affichage seulement si nouvelles valeurs
nouveau = 0

# variables utilisées pour l'affichage du plotter
# qui changera en touchant pin0
etat = 0
contact = 0

anim()
display.show(Image.HAPPY)

while True:

    # modification du plotter lorsque
    # l'on touche pin0
    if pin0.is_touched():
        if contact == 0:
            contact = 1
            etat = (etat + 1) % 2
            if etat == 0:
                display.show('PF')
                print("pile et face")
            else:
                print("fréquence")
                display.show('FREQ')
                for i in range(100):
                    print(('', p/n))
            print(etat)
    else:
        contact = 0

    # réinitialisation des valeurs si on appuie sur bouton B    
    if button_b.was_pressed():
        display.show(Image.HAPPY)
        n = 0
        p = 0
        f = 0

    # nouveau tirage en local (bouton A ou secouer)
    if (button_a.is_pressed() or accelerometer.was_gesture('shake')):
        (n, p) = lancer(n, p)
        nouveau = 1
        sleep(10)
    
    # nouveau tirage par radio
    incoming = radio.receive()
    if incoming == '0':
        n += 1
        nouveau = 1
    if incoming == '1':
        n += 1
        p += 1
        nouveau = 1

    # soit on affiche le nb de piles et de faces (etat == 0)
    # soit on affiche la fréquence de piles (etat == 1)
    if nouveau == 1:
        nouveau = 0
        if etat == 0:
            f = n-p
            print((p, f))
        else:
            if n != 0:
                print(('', p/n))
        print(n)