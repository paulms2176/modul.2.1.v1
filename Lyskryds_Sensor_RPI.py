#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER_EV = 18
GPIO_ECHO_EV = 24
GPIO_TRIGGER_NS = 16
GPIO_ECHO_NS = 22
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_EV, GPIO.OUT)
GPIO.setup(GPIO_ECHO_EV, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_NS, GPIO.OUT)
GPIO.setup(GPIO_ECHO_NS, GPIO.IN)
 
def distanceEV():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_EV, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_EV, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_EV) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_EV) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def distanceNS():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_NS, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_NS, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_NS) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_NS) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance


#Statemachine til beskrivelse af livets gang
from gpiozero import LED
import random

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
EVred=LED(21)
EVgul=LED(20)
EVgreen=LED(12)


print("Test!")
EVred.on()
time.sleep(1)
EVgreen.on()
time.sleep(1)
EVgul.on()
time.sleep(1)
NSred.on()
time.sleep(1)
NSgreen.on()
time.sleep(1)
NSgul.on()
time.sleep(1)
EVred.off()
EVgreen.off()
EVgul.off()
NSred.off()
NSgreen.off()
NSgul.off()
s=0

def redred(x):# Udgangs punkt for lyskrydset
    global s
    s +=1
    print (s)
    print ("NS", distanceNS(), "EV", distanceEV())
    if distanceEV() < 10 and distanceNS() < 10:
        pass
    elif distanceEV() < 10:
        x = "NS"
    elif distanceNS() < 10:
        x = "EV"
    if x=="NS": #Hvis lyskrydset kommer fra NS skal den gå til EV
        x="EV"
        print("NS RED   EV RED")
        NSgul.off()
        EVgul.off()
        NSred.on()
        EVred.on()
        time.sleep(2)
        return EV()
    elif x=="EV": #Hvis lyskrydset kommer fra EV skal den gå til NS
        x="NS"
        print("NS red   EV red")
        NSgul.off()
        EVgul.off()
        NSred.on()
        EVred.on()
        time.sleep(2)
        return NS()
def NS():
    print ("NS", distanceNS(), "EV", distanceEV())
    NSgul.on()
    time.sleep(2)
    return NS_green()

def NS_green():
    print ("NS", distanceNS(), "EV", distanceEV())
    NSred.off()
    NSgul.off()
    NSgreen.on()
    time.sleep(2)
    z = 0
    while distanceNS() < 10:
        time.sleep(2)
        z += 1
        print (z)
        if z > 5:
            break
    return NS_gul()

def NS_gul():
    print ("NS", distanceNS(), "EV", distanceEV())
    NSgreen.off()
    NSgul.on()
    time.sleep(2)
    x = "NS"
    return redred(x)

def EV():
    print ("NS", distanceNS(), "EV", distanceEV())
    EVgul.on()
    time.sleep(2)
    return EV_green()

def EV_green():
    print ("NS", distanceNS(), "EV", distanceEV())
    EVred.off()
    EVgul.off()
    EVgreen.on()
    time.sleep(2)
    z = 0
    while distanceEV() < 10:
        time.sleep(2)
        z += 1
        print (z)
        if z > 5:
            break
    return EV_gul()

def EV_gul():
    print ("NS", distanceNS(), "EV", distanceEV())
    EVgreen.off()
    EVgul.on()
    time.sleep(2)
    x = "EV"
    return redred(x)

state=redred(x="EV")
#while state: state=redred(x="EV")
