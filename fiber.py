from random import random
from time import sleep


def state0():
    print ("hvilken SM fiber vil du bruge?")
    print("1. 1310nm eller 2. 1550nm eller 3. For at stoppe\n")
    x = int(input())
    if x == 1:
        z = 0.35
    elif x == 2:
        z = 0.22
    elif x == 3:
        exit(0)
    return state1(z)

def state1(z):
    print("Hvis du ikke kender Output Power, så brug -2")
    op = float (input ("Output Power i dBm\n"))
    print("Hvis du ikke kender Recieve Sensitivity, så brug -23")
    rs = float (input ("Recieve Sensitivity i dBm\n"))
    bo = op - rs
    print("Brutto overskud i dB er:", bo)
    return state2(z, bo)

def state2(z, bo):
    k = int (input ("Konnekteringer a 0.75dB\n"))
    k1 = k * 0.75
    s = int (input("Splidsninger a 0,3 dB\n"))
    s1 = s * 0.3
    f = int (input("Fiber i km.\n"))
    fdb = f * z
    l = bo - k1 - s1 - fdb
    print("Linkmarginen er:", l)
    return state3(l)

def state3(l):
    print ("Som standart er din sikkerhedsmargin 3")
    sh = int (input("Hvor stor vil du have din sikkerhedsmargin være?\n"))
    print ("Som standart er overskud til raparationer 0.5")
    r = float (input("Hvor stor skal dit overskud til raparationer være?\n"))
    no = l - sh - r
    if no >= 0:
        print('\x1b[4;30;42m' + 'Den er ok og overholder dit fiber budget' + '\x1b[0m')
        print('\x1b[4;30;42m' + 'Netto overskud i dB er:' + str (no) + '\x1b[0m')
        print("")
    elif no < 0:
        print('\x1b[6;30;41m' + 'Den er ikke ok og overholder ikke dit fiber budget' + '\x1b[0m')
        print('\x1b[6;30;41m' + 'Netto underskudet i dB er: ' + str (no) + '\x1b[0m')
        print("")
    return state0()


state=state0    # initial state
while state: state=state()  # starter statemachine
